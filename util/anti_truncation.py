"""
抗截断模块 - 确保流式输出完整性

原理（参考 gcli2api 实现）：
1. 在请求中注入结束标记指令，要求模型输出完整后加 [done] 标记
2. 流式响应时实时检测 [done] 标记
3. 如果流结束但没有 [done]，自动发送续传请求
4. 循环直到检测到 [done] 或达到最大尝试次数
5. 返回内容前移除 [done] 标记

适配 Google Business API 的 streamAssistResponse 格式
"""

import io
import re
import logging
from typing import Optional

logger = logging.getLogger("gemini")


# ==================== 配置 ====================

DONE_MARKER = "[done]"
MAX_CONTINUATION_ATTEMPTS = 3  # 最大续传尝试次数

# 注入到请求中的结束标记指令（放在用户消息末尾）
ANTI_TRUNCATION_INSTRUCTION = f"""

【重要：输出完整性规则】
当你完成完整回答时，必须在输出的最后单独一行输出：{DONE_MARKER}
{DONE_MARKER} 标记表示你的回答已经完全结束，这是必需的结束标记。
无论回答长短，都必须以 {DONE_MARKER} 标记结束。
注意：{DONE_MARKER} 必须单独占一行，前面不要有任何其他字符。"""

# 续传提示词
CONTINUATION_PROMPT = f"""请从刚才被截断的地方继续输出剩余的所有内容。

重要提醒：
1. 不要重复前面已经输出的内容
2. 直接继续输出，无需任何前言或解释
3. 当你完整完成所有内容输出后，必须在最后一行单独输出：{DONE_MARKER}
4. {DONE_MARKER} 标记表示你的回答已经完全结束，这是必需的结束标记

现在请继续输出："""


# ==================== 工具函数 ====================

def check_done_marker(text: str) -> bool:
    """检测文本中是否包含 DONE_MARKER"""
    if not text:
        return False
    return DONE_MARKER.lower() in text.lower()


def remove_done_marker(text: str) -> str:
    """从文本中移除 DONE_MARKER（保留其他内容）"""
    if not text:
        return text
    # 使用正则匹配，处理可能的空白字符
    pattern = re.compile(r"\s*\[done\]\s*", re.IGNORECASE)
    return pattern.sub("", text)


def inject_anti_truncation_instruction(text_content: str) -> str:
    """
    在请求文本末尾注入抗截断指令

    Args:
        text_content: 原始请求文本

    Returns:
        注入指令后的文本
    """
    # 检查是否已包含指令（避免重复注入）
    if DONE_MARKER in text_content:
        return text_content

    return f"{text_content}{ANTI_TRUNCATION_INSTRUCTION}"


def build_continuation_text(original_text: str, collected_content: str) -> str:
    """
    构建续传请求的文本内容

    Args:
        original_text: 原始请求文本
        collected_content: 已收集的响应内容

    Returns:
        续传请求的文本
    """
    # 构建上下文摘要
    content_summary = ""
    if collected_content:
        if len(collected_content) > 200:
            content_summary = f'\n\n前面你已经输出了约 {len(collected_content)} 个字符的内容，结尾是：\n"...{collected_content[-100:]}"'
        else:
            content_summary = f'\n\n前面你已经输出的内容是：\n"{collected_content}"'

    return f"{original_text}\n\n{CONTINUATION_PROMPT}{content_summary}"


def clean_done_marker_from_text(text: str) -> str:
    """
    从文本中清理 done 标记

    用于流式响应的实时处理
    """
    return remove_done_marker(text)


# ==================== 抗截断内容收集器 ====================

class AntiTruncationCollector:
    """
    抗截断内容收集器

    用于在流式处理中收集内容和检测 [done] 标记
    """

    def __init__(self, max_attempts: int = MAX_CONTINUATION_ATTEMPTS):
        self.max_attempts = max_attempts
        self.current_attempt = 0
        self.collected_content = io.StringIO()
        self.found_done_marker = False

    def append_content(self, text: str):
        """追加内容"""
        if text:
            self.collected_content.write(text)
            # 实时检测 done 标记
            if check_done_marker(text):
                self.found_done_marker = True
                logger.debug(f"[ANTI-TRUNCATION] 在内容中检测到 [done] 标记")

    def get_collected_content(self) -> str:
        """获取已收集的内容"""
        return self.collected_content.getvalue()

    def check_accumulated_done_marker(self) -> bool:
        """检查累积内容中是否有 done 标记（用于跨 chunk 检测）"""
        if not self.found_done_marker:
            accumulated = self.get_collected_content()
            if check_done_marker(accumulated):
                self.found_done_marker = True
                logger.info(f"[ANTI-TRUNCATION] 在累积内容中检测到 [done] 标记")
        return self.found_done_marker

    def should_continue(self) -> bool:
        """检查是否需要续传"""
        return not self.found_done_marker and self.current_attempt < self.max_attempts

    def start_new_attempt(self):
        """开始新的尝试"""
        self.current_attempt += 1
        logger.info(f"[ANTI-TRUNCATION] 开始第 {self.current_attempt}/{self.max_attempts} 次尝试")

    def reset_for_continuation(self):
        """为续传重置状态（保留已收集的内容）"""
        # 不清空 collected_content，续传时需要用到
        pass

    def cleanup(self):
        """清理资源"""
        self.collected_content.close()
        self.collected_content = io.StringIO()


# ==================== 测试 ====================

if __name__ == "__main__":
    # 测试 done 标记检测和清理
    test_texts = [
        "这是一段正常的文本",
        "这是一段带标记的文本\n[done]",
        "文本内容 [DONE] 还有更多",
        "  [Done]  ",
    ]

    print("=== done 标记检测和清理测试 ===")
    for text in test_texts:
        has_marker = check_done_marker(text)
        cleaned = remove_done_marker(text)
        print(f"原文: {repr(text)}")
        print(f"  有标记: {has_marker}")
        print(f"  清理后: {repr(cleaned)}")
        print()

    # 测试指令注入
    print("=== 指令注入测试 ===")
    original = "请帮我写一首诗"
    injected = inject_anti_truncation_instruction(original)
    print(f"原始请求长度: {len(original)}")
    print(f"注入后长度: {len(injected)}")
    print(f"注入的内容:\n{injected}")
    print()

    # 测试续传文本构建
    print("=== 续传文本构建测试 ===")
    continuation = build_continuation_text("写一首诗", "玫瑰花开满园香，蝴蝶翩翩舞飞扬...")
    print(f"续传文本:\n{continuation}")
