"""
Business API 请求规范化模块

处理 Google Business API (biz-discoveryengine) 的请求规范化
包括模型配置、思考配置等

注意：Business API 的请求格式与标准 Gemini API 不同
- 使用 assistGenerationConfig 而不是 generationConfig
- 使用 streamAssistRequest 结构
"""

import logging
from typing import Any, Dict, Optional

from core.model_config import (
    get_base_model_name,
    get_thinking_settings,
    is_search_model,
    parse_model_features,
)

logger = logging.getLogger("gemini")


# ==================== Business API 配置构建 ====================

def build_assist_generation_config(
    model_name: str,
    base_model_id: Optional[str] = None,
) -> Dict[str, Any]:
    """
    构建 Business API 的 assistGenerationConfig

    Args:
        model_name: 完整模型名称（可能包含前缀/后缀）
        base_model_id: 基础模型ID（如果已知）

    Returns:
        assistGenerationConfig 字典
    """
    config = {}

    # 1. 设置模型ID
    if base_model_id:
        config["modelId"] = base_model_id
    else:
        base_model = get_base_model_name(model_name)
        if base_model:
            config["modelId"] = base_model

    # 2. 获取思考配置
    thinking_budget, include_thoughts = get_thinking_settings(model_name)

    # 3. 如果有思考配置，添加到 config
    # 注意：Business API 可能使用不同的字段名，这里预留接口
    if thinking_budget is not None:
        # Business API 的思考配置（字段名需要根据实际 API 确认）
        config["thinkingConfig"] = {
            "thinkingBudget": thinking_budget,
            "includeThoughts": include_thoughts,
        }
        logger.debug(f"[GEMINI_FIX] 设置思考配置: budget={thinking_budget}, include={include_thoughts}")

    return config


def build_tools_spec(
    model_name: str,
    enable_image_generation: bool = False,
    enable_video_generation: bool = False,
) -> Dict[str, Any]:
    """
    构建 Business API 的 toolsSpec

    Args:
        model_name: 模型名称
        enable_image_generation: 是否启用图片生成
        enable_video_generation: 是否启用视频生成

    Returns:
        toolsSpec 字典
    """
    tools_spec = {
        "toolRegistry": "default_tool_registry",
    }

    # 如果是搜索模型或默认启用搜索
    if is_search_model(model_name):
        tools_spec["webGroundingSpec"] = {}
        logger.debug(f"[GEMINI_FIX] 启用搜索功能")
    else:
        # 默认也启用搜索（根据原代码逻辑）
        tools_spec["webGroundingSpec"] = {}

    # 图片/视频生成
    if enable_image_generation:
        tools_spec["imageGenerationSpec"] = {}
    if enable_video_generation:
        tools_spec["videoGenerationSpec"] = {}

    return tools_spec


# ==================== 请求规范化 ====================

def normalize_business_api_request(
    body: Dict[str, Any],
    model_name: str,
    enable_image_generation: bool = False,
    enable_video_generation: bool = False,
) -> Dict[str, Any]:
    """
    规范化 Business API 请求

    Args:
        body: 原始请求体
        model_name: 完整模型名称
        enable_image_generation: 是否启用图片生成
        enable_video_generation: 是否启用视频生成

    Returns:
        规范化后的请求体
    """
    result = body.copy()
    features = parse_model_features(model_name)

    # 确保 streamAssistRequest 存在
    if "streamAssistRequest" not in result:
        result["streamAssistRequest"] = {}

    stream_request = result["streamAssistRequest"]

    # 1. 设置 assistGenerationConfig
    assist_config = build_assist_generation_config(
        model_name,
        base_model_id=features["base_model"],
    )
    if assist_config:
        stream_request["assistGenerationConfig"] = assist_config

    # 2. 设置 toolsSpec
    tools_spec = build_tools_spec(
        model_name,
        enable_image_generation=enable_image_generation,
        enable_video_generation=enable_video_generation,
    )
    stream_request["toolsSpec"] = tools_spec

    # 3. 记录日志
    logger.debug(f"[GEMINI_FIX] 规范化请求 - 模型: {model_name} -> {features['base_model']}")
    logger.debug(f"[GEMINI_FIX] 特性: fake_stream={features['is_fake_stream']}, "
                f"anti_truncation={features['is_anti_truncation']}, "
                f"thinking={features['thinking_mode']}, "
                f"search={features['is_search']}")

    return result


# ==================== 响应清理 ====================

def clean_response_text(text: str) -> str:
    """
    清理响应文本

    - 移除抗截断的 [done] 标记
    - 其他必要的清理

    Args:
        text: 原始响应文本

    Returns:
        清理后的文本
    """
    if not text:
        return text

    # 移除 [done] 标记
    import re
    pattern = re.compile(r"\s*\[done\]\s*", re.IGNORECASE)
    cleaned = pattern.sub("", text)

    return cleaned.strip()


# ==================== 辅助函数 ====================

def get_effective_model_id(model_name: str, model_mapping: Dict[str, str]) -> Optional[str]:
    """
    获取有效的模型ID（用于 API 请求）

    Args:
        model_name: 请求的模型名称
        model_mapping: 模型映射字典

    Returns:
        有效的模型ID，如果是 auto 则返回 None
    """
    # 先检查映射表
    if model_name in model_mapping:
        return model_mapping[model_name]

    # 否则解析基础模型名
    base_model = get_base_model_name(model_name)

    # gemini-auto 返回 None
    if base_model == "gemini-auto" or model_name == "gemini-auto":
        return None

    return base_model


# ==================== 测试 ====================

if __name__ == "__main__":
    # 测试 assistGenerationConfig 构建
    test_models = [
        "gemini-2.5-pro",
        "gemini-2.5-pro-nothinking",
        "gemini-2.5-flash-maxthinking",
        "流式抗截断/gemini-2.5-pro-maxthinking-search",
    ]

    for model in test_models:
        print(f"模型: {model}")
        config = build_assist_generation_config(model)
        print(f"  assistGenerationConfig: {config}")

        tools = build_tools_spec(model)
        print(f"  toolsSpec: {tools}")
        print()
