---
title: Gemini Business
emoji: 💎
colorFrom: pink
colorTo: blue
sdk: docker
pinned: false
license: mit
---

#  Gemini Business

将 Google Gemini Business 自动注册、Token 刷新、API 转换为 OpenAI 兼容接口，实现全自动化处理。

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)


## ✨ 功能特性

### 核心功能
- ✅ **OpenAI API 完全兼容** - 无缝对接现有工具
- ✅ **流式响应支持** - 实时输出
- ✅ **多模态支持** - 支持 100+ 种文件类型（图片、PDF、Office 文档、音频、视频、代码等）
- ✅ **图片生成 & 图生图** - 支持 `gemini-3-pro-preview` 模型
- ✅ **智能文件处理** - 自动识别文件类型，支持 URL 和 Base64 格式

### 多账户管理
- ✅ **多账户负载均衡** - 支持多账户轮询，故障自动转移
- ✅ **智能熔断机制** - 账户连续失败自动熔断，429限流10分钟后自动恢复
- ✅ **三层重试策略** - 新会话重试、请求重试、账户切换
- ✅ **智能会话复用** - 自动管理对话历史，缓存过期自动清理
- ✅ **在线配置管理** - Web界面编辑账户配置，实时生效
- ✅ **账户过期自动禁用** - 设置过期时间，过期后自动禁用不可选用
- ✅ **手动禁用/启用** - 管理面板一键禁用/启用账户
- ✅ **错误永久禁用** - 普通错误触发熔断后永久禁用，需手动启用恢复

### 系统功能
- ✅ **JWT自动管理** - 无需手动刷新令牌
- 📊 **可视化管理面板** - 实时监控账户状态、过期时间、失败计数、累计对话次数
- 📈 **账户使用统计** - 自动统计每个账户累计对话次数，持久化保存
- 📝 **公开日志系统** - 实时查看服务运行状态（内存最多3000条，自动淘汰）
- 🔐 **双重认证保护** - API_KEY 保护聊天接口，ADMIN_KEY 保护管理面板
- 📡 **实时状态监控** - 公开统计接口，实时查看服务状态和请求统计

### 自动注册 & 登录刷新
- ✅ **一键批量注册** - 管理面板一键批量注册新账户
- ✅ **自动获取配置** - 自动完成邮箱验证、获取 Cookie 和配置信息
- ✅ **崩溃自动恢复** - Chrome 页面崩溃时自动开新标签页重试
- ✅ **过期自动刷新** - 账户即将过期时自动刷新登录（每30分钟检查一次）
- ✅ **Xvfb 虚拟显示器** - Docker 环境下无需真实显示器即可运行 Chrome
- ✅ **代理池支持** - 支持配置代理池，避免 IP 限制，同时支持代理检测自动切换和重试（代理检测属于启动 chrome 前置检测）

### 性能优化
- ⚡ **异步文件 I/O** - 避免阻塞事件循环，提升并发性能
- ⚡ **HTTP 连接池优化** - 提升高并发场景下的稳定性
- ⚡ **图片并行下载** - 多图场景下显著提升响应速度
- ⚡ **智能锁优化** - 减少锁竞争，提升账户选择效率
- ⚡ **会话并发控制** - Session 级别锁，避免对话冲突

## 📸 功能展示

### 图片生成效果

<table>
  <tr>
    <td><img src="https://github.com/user-attachments/assets/d6837897-63f2-4a17-ba4a-f59030e37018" alt="图片生成示例1" width="800"/></td>
    <td><img src="https://github.com/user-attachments/assets/dc597631-b00b-4307-bba1-c0ed21db0e1b" alt="图片生成示例2" width="800"/></td>
  </tr>
  <tr>
    <td><img src="https://github.com/user-attachments/assets/4e3a1ffa-dea9-4207-ac9b-bb32f8e83c6f" alt="图片生成示例3" width="800"/></td>
    <td><img src="https://github.com/user-attachments/assets/53a30edd-c2ec-4cd3-a0bd-ccf68884472a" alt="图片生成示例4" width="800"/></td>
  </tr>
</table>

### 管理面板

<table>
  <tr>
    <td><img src="https://github.com/user-attachments/assets/d0548b2b-b57e-4857-8ed0-b48b4daef34f" alt="管理面板1" width="800"/></td>
    <td><img src="https://github.com/user-attachments/assets/6b2aff95-e48f-412f-9e6e-2e893595b6dd" alt="管理面板2" width="800"/></td>
  </tr>
</table>

### 日志系统

<table>
  <tr>
    <td><img src="https://github.com/user-attachments/assets/4c9c38c4-6322-4057-b5f0-a10f8b82b6ae" alt="日志系统1" width="800"/></td>
    <td><img src="https://github.com/user-attachments/assets/095b86d7-3924-4258-954a-85bda9e8478e" alt="日志系统2" width="800"/></td>
  </tr>
</table>

## 🚀 快速开始

### 方法一: Docker Compose 部署（当前仅支持 linux/amd64 架构）

```bash
# 1.下载 docker-compose.yml 文件
curl -O https://raw.githubusercontent.com/linlee996/gemini-business/main/docker-compose.yml

# 2.编辑 docker-compose.yml， environment 中填入管理员信息、google business 登录地址（其他配置可启动后配置）
vim docker-compose.yml

# 3.启动服务
docker-compose up -d
```

```bash
# 1. 克隆项目
git clone https://github.com/linlee996/gemini-business.git
cd gemini-business

# 2. 构建并运行
docker build -t gemini-business .
docker run -d \
  -p 7860:7860 \
  -e PATH_PREFIX=path_prefix \
  -e ADMIN_KEY=your_admin_key \
  -e API_KEY=your_api_key \
  -e LOGO_URL=https://your-domain.com/logo.png \
  -e CHAT_URL=https://your-chat-app.com \
  gemini-business
```

### 方法二: 本地运行

```bash
# 1. 安装依赖
uv sync

# 2. 配置环境变量
cp .env.example .env
# 编辑 .env 文件，填入实际配置

# 3. 启动服务
uv run main.py
```

服务将在 `http://localhost:7860` 启动

## ⚙️ 配置说明

### 必需的环境变量

```bash
# 账户配置（必需）
ACCOUNTS_CONFIG='[{"secure_c_ses":"your_cookie","csesidx":"your_idx","config_id":"your_config"}]'

# 路径前缀（必需）
PATH_PREFIX=path_prefix

# 管理员密钥（必需）
ADMIN_KEY=your_admin_key

# API访问密钥（可选，推荐设置）
API_KEY=your_api_key

# 图片URL生成（可选，推荐设置）
BASE_URL=https://your-domain.com

# 全局代理（可选）
PROXY=http://127.0.0.1:7890

# 公开展示配置（可选）
LOGO_URL=https://your-domain.com/logo.png
CHAT_URL=https://your-chat-app.com
MODEL_NAME=gemini-business

# 重试配置（可选）
MAX_NEW_SESSION_TRIES=5        # 新会话尝试账户数（默认5）
MAX_REQUEST_RETRIES=3          # 请求失败重试次数（默认3）
MAX_ACCOUNT_SWITCH_TRIES=5     # 每次重试查找账户次数（默认5）
ACCOUNT_FAILURE_THRESHOLD=3    # 账户失败阈值，达到后熔断（默认3）
RATE_LIMIT_COOLDOWN_SECONDS=600 # 429限流冷却时间，秒（默认600=10分钟）
SESSION_CACHE_TTL_SECONDS=3600 # 会话缓存过期时间，秒（默认3600=1小时）

# 自动注册配置（必须，需要 Docker 部署）
LOGIN_URL=https://auth.business.gemini.google/login?continueUrl=...  # Google 登录入口
GOOGLE_MAIL=noreply-googlecloud@google.com                          # Google 验证码发件邮箱
MAIL_API=https://your-temp-mail-api.com                             # 临时邮箱 API 地址
MAIL_ADMIN_KEY=your-mail-admin-key                                  # 邮箱 API 管理密钥
EMAIL_DOMAIN=domain1.com,domain2.org                                # 邮箱域名（逗号分隔）
```

### 重试机制说明

系统提供三层重试保护：

1. **新会话创建重试**：创建新对话时，如果账户失败，自动切换到其他账户（最多尝试5个）
2. **请求失败重试**：对话过程中出错，自动重试并切换账户（最多重试3次）
3. **智能熔断机制**：
   - 账户连续失败3次 → 自动标记为不可用
   - **429限流错误**：冷却10分钟后自动恢复
   - **普通错误**：永久禁用，需手动启用
   - JWT失败和请求失败都会触发熔断

### 自动注册配置说明

自动注册功能需要以下配置：

| 配置项 | 说明 | 示例 |
|--------|------|------|
| `LOGIN_URL` | Google Business 登录入口 URL | 完整的登录链接 |
| `GOOGLE_MAIL` | Google 验证码发件邮箱 | `noreply-googlecloud@google.com` |
| `MAIL_API` | 临时邮箱服务 API 地址 | Cloudflare Worker 邮箱服务 |
| `MAIL_ADMIN_KEY` | 邮箱 API 管理密钥 | 用于创建和查询临时邮箱 |
| `EMAIL_DOMAIN` | 邮箱域名列表 | 多个域名用逗号分隔 |

**使用方法**：
1. 配置好以上环境变量
2. 使用 Docker 部署（包含 Chrome 和 Xvfb）
3. 在管理面板点击「注册新账户」按钮
4. 选择域名和数量，开始批量注册
5. 注册成功的账户自动添加到 `accounts.json`

### 多账户配置示例

```bash
ACCOUNTS_CONFIG='[
  {
    "id": "account_1",
    "secure_c_ses": "CSE.Ad...",
    "csesidx": "498...",
    "config_id": "0cd...",
    "host_c_oses": "COS.Af...",
    "expires_at": "2025-12-23 23:03:20"
  },
  {
    "id": "account_2",
    "secure_c_ses": "CSE.Ad...",
    "csesidx": "208...",
    "config_id": "782..."
  }
]'
```

**配置字段说明**:
- `secure_c_ses` (必需): `__Secure-C_SES` Cookie 值
- `csesidx` (必需): 会话索引
- `config_id` (必需): 配置 ID
- `id` (可选): 账户标识
- `host_c_oses` (可选): `__Host-C_OSES` Cookie 值
- `expires_at` (可选): 过期时间，格式 `YYYY-MM-DD HH:MM:SS`

**提示**: 参考项目根目录的 `.env.example` 和 `accounts_config.example.json` 文件

## 🔧 获取配置参数

1. 访问 [Google Gemini Business](https://business.gemini.google)
2. 打开浏览器开发者工具 (F12)
3. 切换到 **Application** → **Cookies**，找到:
   - `__Secure-C_SES` → `secure_c_ses`
   - `__Host-C_OSES` → `host_c_oses` (可选)
4. 切换到 **Network** 标签，刷新页面
5. 找到 `streamGenerate` 请求，查看 Payload:
   - `csesidx` → `csesidx`
   - `configId` → `config_id`

## 📖 API 使用

### 支持的模型

| 模型名称                 | 说明                   | 图片生成 |
| ------------------------ | ---------------------- | -------- |
| `gemini-auto`            | 自动选择最佳模型(默认) | ❌        |
| `gemini-2.5-flash`       | Flash 2.5 - 快速响应   | ❌        |
| `gemini-2.5-pro`         | Pro 2.5 - 高质量输出   | ❌        |
| `gemini-3-flash-preview` | Flash 3 预览版         | ❌        |
| `gemini-3-pro-preview`   | Pro 3 预览版           | ✅        |

### 访问端点

| 端点                                     | 方法   | 说明                        |
| ---------------------------------------- | ------ | --------------------------- |
| `/{PATH_PREFIX}/v1/models`               | GET    | 获取模型列表                |
| `/{PATH_PREFIX}/v1/chat/completions`     | POST   | 聊天接口（需API_KEY）       |
| `/{PATH_PREFIX}`                   | GET    | 管理面板（需ADMIN_KEY）     |
| `/{PATH_PREFIX}/accounts`          | GET    | 获取账户状态（需ADMIN_KEY） |
| `/{PATH_PREFIX}/accounts-config`   | GET    | 获取账户配置（需ADMIN_KEY） |
| `/{PATH_PREFIX}/accounts-config`   | PUT    | 更新账户配置（需ADMIN_KEY） |
| `/{PATH_PREFIX}/accounts/{id}`     | DELETE | 删除指定账户（需ADMIN_KEY） |
| `/{PATH_PREFIX}/accounts/{id}/disable` | PUT | 禁用指定账户（需ADMIN_KEY） |
| `/{PATH_PREFIX}/accounts/{id}/enable`  | PUT | 启用指定账户（需ADMIN_KEY） |
| `/{PATH_PREFIX}/log`               | GET    | 获取系统日志（需ADMIN_KEY） |
| `/{PATH_PREFIX}/log`               | DELETE | 清空系统日志（需ADMIN_KEY） |
| `/public/log/html`                       | GET    | 公开日志页面（无需认证）    |
| `/public/stats`                          | GET    | 公开统计信息（无需认证）    |
| `/public/stats/html`                     | GET    | 实时状态监控页面（无需认证）|

**访问示例**：

假设你的配置为：
- Space URL: `https://your-space.hf.space`
- PATH_PREFIX: `my_prefix`
- ADMIN_KEY: `my_admin_key`

则访问地址为：
- **管理面板**: `https://your-space.hf.space/my_prefix?key=my_admin_key`
- **公开日志**: `https://your-space.hf.space/public/log/html`
- **API 端点**: `https://your-space.hf.space/my_prefix/v1/chat/completions`

### 基本对话

```bash
curl -X POST http://localhost:7860/v1/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer your_api_key" \
  -d '{
    "model": "gemini-2.5-flash",
    "messages": [
      {"role": "user", "content": "Hello!"}
    ],
    "stream": true
  }'
```

### 多模态输入（支持 100+ 种文件类型）

本项目支持图片、PDF、Office 文档、音频、视频、代码等 100+ 种文件类型。详细列表请查看 [支持的文件类型清单](docs/SUPPORTED_FILE_TYPES.md)。

#### 图片输入

```bash
# Base64 格式
curl -X POST http://localhost:7860/v1/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer your_api_key" \
  -d '{
    "model": "gemini-2.5-pro",
    "messages": [
      {
        "role": "user",
        "content": [
          {"type": "text", "text": "这张图片里有什么?"},
          {"type": "image_url", "image_url": {"url": "data:image/jpeg;base64,<base64_encoded_image>"}}
        ]
      }
    ]
  }'

# URL 格式（自动下载并转换）
curl -X POST http://localhost:7860/v1/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer your_api_key" \
  -d '{
    "model": "gemini-2.5-pro",
    "messages": [
      {
        "role": "user",
        "content": [
          {"type": "text", "text": "分析这张图片"},
          {"type": "image_url", "image_url": {"url": "https://example.com/image.jpg"}}
        ]
      }
    ]
  }'
```

#### PDF 文档

```bash
curl -X POST http://localhost:7860/v1/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer your_api_key" \
  -d '{
    "model": "gemini-2.5-pro",
    "messages": [
      {
        "role": "user",
        "content": [
          {"type": "text", "text": "总结这个PDF的内容"},
          {"type": "image_url", "image_url": {"url": "https://example.com/document.pdf"}}
        ]
      }
    ]
  }'
```

#### Office 文档（Word、Excel、PowerPoint）

```bash
# Word 文档
curl -X POST http://localhost:7860/v1/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer your_api_key" \
  -d '{
    "model": "gemini-2.5-pro",
    "messages": [
      {
        "role": "user",
        "content": [
          {"type": "text", "text": "总结这个Word文档"},
          {"type": "image_url", "image_url": {"url": "https://example.com/document.docx"}}
        ]
      }
    ]
  }'

# Excel 表格
curl -X POST http://localhost:7860/v1/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer your_api_key" \
  -d '{
    "model": "gemini-2.5-pro",
    "messages": [
      {
        "role": "user",
        "content": [
          {"type": "text", "text": "分析这个Excel数据"},
          {"type": "image_url", "image_url": {"url": "https://example.com/data.xlsx"}}
        ]
      }
    ]
  }'
```

#### 音频文件（语音转录）

```bash
curl -X POST http://localhost:7860/v1/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer your_api_key" \
  -d '{
    "model": "gemini-2.5-pro",
    "messages": [
      {
        "role": "user",
        "content": [
          {"type": "text", "text": "转录这段音频"},
          {"type": "image_url", "image_url": {"url": "https://example.com/audio.mp3"}}
        ]
      }
    ]
  }'
```

#### 视频文件（场景分析）

```bash
curl -X POST http://localhost:7860/v1/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer your_api_key" \
  -d '{
    "model": "gemini-2.5-pro",
    "messages": [
      {
        "role": "user",
        "content": [
          {"type": "text", "text": "描述这个视频的内容"},
          {"type": "image_url", "image_url": {"url": "https://example.com/video.mp4"}}
        ]
      }
    ]
  }'
```

**支持的文件类型**（12 个分类，100+ 种格式）：

- 🖼️ **图片文件** - 11 种格式（PNG, JPEG, WebP, GIF, BMP, TIFF, SVG, ICO, HEIC, HEIF, AVIF）
- 📄 **文档文件** - 9 种格式（PDF, TXT, Markdown, HTML, XML, CSV, TSV, RTF, LaTeX）
- 📊 **Microsoft Office** - 6 种格式（.docx, .doc, .xlsx, .xls, .pptx, .ppt）
- 📝 **Google Workspace** - 3 种格式（Docs, Sheets, Slides）
- 💻 **代码文件** - 19 种语言（Python, JavaScript, TypeScript, Java, C/C++, Go, Rust, PHP, Ruby, Swift, Kotlin, Scala, Shell, PowerShell, SQL, R, MATLAB 等）
- 🎨 **Web 开发** - 8 种格式（CSS, SCSS, LESS, JSON, YAML, TOML, Vue, Svelte）
- 🎵 **音频文件** - 10 种格式（MP3, WAV, AAC, M4A, OGG, FLAC, AIFF, WMA, OPUS, AMR）
- 🎬 **视频文件** - 10 种格式（MP4, MOV, AVI, MPEG, WebM, FLV, WMV, MKV, 3GPP, M4V）
- 📦 **数据文件** - 6 种格式（JSON, JSONL, CSV, TSV, Parquet, Avro）
- 🗜️ **压缩文件** - 5 种格式（ZIP, RAR, 7Z, TAR, GZ）
- 🔧 **配置文件** - 5 种格式（YAML, TOML, INI, ENV, Properties）
- 📚 **电子书** - 2 种格式（EPUB, MOBI）

完整列表和使用示例请查看 [支持的文件类型清单](docs/SUPPORTED_FILE_TYPES.md)

### 图片生成

```bash
curl -X POST http://localhost:7860/v1/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer your_api_key" \
  -d '{
    "model": "gemini-3-pro-preview",
    "messages": [
      {"role": "user", "content": "画一只可爱的猫咪"}
    ]
  }'
```

### 图生图（Image-to-Image）

```bash
curl -X POST http://localhost:7860/v1/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer your_api_key" \
  -d '{
    "model": "gemini-3-pro-preview",
    "messages": [
      {
        "role": "user",
        "content": [
          {"type": "text", "text": "将这张图片改成水彩画风格"},
          {"type": "image_url", "image_url": {"url": "data:image/jpeg;base64,<base64_encoded_image>"}}
        ]
      }
    ]
  }'
```

## ❓ 常见问题

### 1. 如何在线编辑账户配置？

访问管理面板 `/{PATH_PREFIX}?key=YOUR_ADMIN_KEY`，点击"编辑配置"按钮：
- ✅ 实时编辑 JSON 格式配置
- ✅ 保存后立即生效，无需重启
- ✅ 配置保存到 `accounts.json` 文件
- ⚠️ 重启后从环境变量 `ACCOUNTS_CONFIG` 重新加载

**建议**：在线修改后，同步更新环境变量 `ACCOUNTS_CONFIG`，避免重启后配置丢失。

### 2. 账户熔断后如何恢复？

账户连续失败3次后会自动熔断（标记为不可用）：
- ⏰ **429限流错误**：冷却10分钟后自动恢复（可通过 `RATE_LIMIT_COOLDOWN_SECONDS` 配置）
- 🔄 **普通错误**：永久禁用，需在管理面板手动点击"启用"按钮恢复
- ✅ **成功后**：失败计数重置为0，账户恢复正常

可在管理面板实时查看账户状态和失败计数。

### 3. 账户禁用功能有哪些？

管理面板提供完整的账户禁用管理功能，不同禁用状态有不同的恢复方式：

#### 📋 **账户状态说明**

| 状态 | 显示 | 颜色 | 自动恢复 | 恢复方式 | 倒计时 |
|------|------|------|---------|---------|--------|
| **正常** | 正常/即将过期 | 绿色/橙色 | - | - | ❌ |
| **过期禁用** | 过期禁用 | 灰色 | ❌ | 修改过期时间 | ❌ |
| **手动禁用** | 手动禁用 | 灰色 | ❌ | 点击"启用"按钮 | ❌ |
| **错误禁用** | 错误禁用 | 红色 | ❌ | 点击"启用"按钮 | ❌ |
| **429限流** | 429限流 | 橙色 | ✅ 10分钟 | 自动恢复或点击"启用" | ✅ |

#### ⚙️ **功能说明**

1. **账户过期自动禁用**
   - 在账户配置中设置 `expires_at` 字段（格式：`YYYY-MM-DD HH:MM:SS`）
   - 过期后账户自动禁用，不参与轮询选择
   - 页面显示灰色半透明卡片，仅保留"删除"按钮
   - 需要修改过期时间才能重新启用

2. **手动禁用/启用**
   - 管理面板每个账户卡片都有"禁用"按钮
   - 点击后立即禁用，不参与轮询选择
   - 显示灰色半透明卡片，提供"启用"+"删除"按钮
   - 点击"启用"按钮即可恢复

3. **错误自动禁用（永久）**
   - 账户连续失败3次触发（非429错误）
   - 自动标记为不可用，永久禁用
   - 显示红色半透明卡片，提供"启用"+"删除"按钮
   - 需要手动点击"启用"按钮恢复

4. **429限流自动禁用（临时）**
   - 账户连续遇到429错误3次触发
   - 自动冷却10分钟（可配置 `RATE_LIMIT_COOLDOWN_SECONDS`）
   - 显示橙色卡片，带倒计时显示（如：`567秒 (429限流)`）
   - 冷却期过后自动恢复，或手动点击"启用"立即恢复

#### 💡 **使用建议**

- **临时维护**：使用"手动禁用"功能暂时停用账户
- **账户轮换**：设置过期时间，到期自动禁用
- **故障排查**：错误禁用的账户需检查后再手动启用
- **429限流**：耐心等待10分钟自动恢复，或检查请求频率

### 4. 账户对话次数统计如何工作？

系统自动统计每个账户的累计对话次数，无需手动操作。

#### 📊 **统计说明**

- **自动计数**：每次聊天请求成功后自动 +1
- **持久化保存**：保存到 `data/stats.json` 文件，重启不丢失
- **实时显示**：管理面板账户卡片实时显示累计次数
- **数据位置**：`data/stats.json` → `account_conversations` 字段

#### 📈 **显示位置**

管理面板账户卡片中，"剩余时长"行下方：
```
过期时间: 2025-12-31 23:59:59
剩余时长: 72.5 小时
累计对话: 123 次  ← 蓝色加粗显示
```

#### 💡 **数据说明**

- 统计范围：仅统计成功的对话请求
- 失败请求：不计入累计次数
- 数据格式：`{"account_id": conversation_count}`
- 重置方式：目前需要手动编辑 `data/stats.json` 文件

### 5. 图片生成后在哪里找到文件?

- **临时存储**: 图片保存在 `./data/images/`，可通过 URL 访问
- **重启后会丢失**，建议使用持久化存储

### 6. 如何设置 BASE_URL?

**自动检测**(推荐):
- 不设置 `BASE_URL` 环境变量
- 系统自动从请求头检测域名

**手动设置**:
```bash
BASE_URL=https://your-domain.com
```

**使用反向代理**:

如果你使用自己的域名反向代理到 HuggingFace Space，可以通过以下方式配置：

**Nginx 配置示例**:
```nginx
location / {
    proxy_pass https://your-username-space-name.hf.space;
    proxy_set_header Host your-username-space-name.hf.space;
    proxy_ssl_server_name on;
}
```

**Deno Deploy 配置示例**:
```typescript
async function handler(request: Request): Promise<Response> {
  const url = new URL(request.url);
  url.host = 'your-username-space-name.hf.space';
  return fetch(new Request(url, request));
}

Deno.serve(handler);
```

配置反向代理后，将 `BASE_URL` 设置为你的自定义域名即可。

### 7. API_KEY 和 ADMIN_KEY 的区别?

- **API_KEY**: 保护聊天接口 (`/v1/chat/completions`)
- **ADMIN_KEY**: 保护管理面板 (`/` 或 `/{PATH_PREFIX}`)

可以设置相同的值，也可以分开

### 8. 如何查看日志?

- **公开日志**: 访问 `/public/log/html` (无需密钥)
- **管理面板**: 访问 `/?key=YOUR_ADMIN_KEY` 或 `/{PATH_PREFIX}?key=YOUR_ADMIN_KEY`

日志系统说明：
- 内存存储最多 3000 条日志
- 超过上限自动删除最旧的日志
- 重启后清空（内存存储）
- 可通过 API 手动清空日志

## 🔧 油猴脚本使用说明

本项目提供油猴脚本辅助获取配置参数，使用前需要配置 TamperMonkey：

### TamperMonkey 设置

1. **配置模式**：改为 `高级`
2. **安全设置**：允许脚本访问 Cookie 改为 `All`

### Google Chrome 额外设置

1. 打开油猴扩展设置
2. 启用 **允许运行用户脚本**
3. 设置 **有权访问的网站** 权限

配置完成后即可使用脚本自动获取 `secure_c_ses`、`csesidx`、`config_id` 等参数。

---

## 📁 项目结构

```
gemini-business2api/
├── main.py                        # 主程序入口
├── core/                          # 核心模块
│   ├── __init__.py
│   ├── auth.py                    # API 认证装饰器
│   ├── session_auth.py            # Session 认证（管理面板）
│   ├── account.py                 # 账户管理
│   ├── config.py                  # 配置管理
│   ├── google_api.py              # Google API 封装
│   ├── message.py                 # 消息处理
│   ├── jwt.py                     # JWT 管理
│   ├── uptime.py                  # Uptime 监控
│   ├── register_service.py        # 🆕 自动注册服务
│   └── login_service.py           # 🆕 自动登录刷新服务
├── util/                          # 工具模块
│   ├── streaming_parser.py        # 流式 JSON 解析器
│   ├── gemini_auth_utils.py       # 🆕 认证工具（注册/登录公共逻辑）
│   └── template_helpers.py        # 模板辅助函数
├── templates/                     # HTML 模板
│   ├── admin/                     # 管理面板模板
│   └── auth/                      # 登录页面模板
├── static/                        # 静态文件（CSS/JS）
├── docs/                          # 文档目录
│   └── SUPPORTED_FILE_TYPES.md    # 支持的文件类型清单
├── data/                          # 运行时数据目录
│   ├── accounts.json              # 账户配置（自动注册后保存）
│   ├── settings.yaml              # 系统设置
│   ├── stats.json                 # 统计数据
│   └── images/                    # 生成的图片
├── script/                        # 辅助脚本
│   ├── copy-config.js             # 油猴脚本：复制配置
│   └── download-config.js         # 油猴脚本：下载配置
├── Dockerfile                     # Docker 构建（含 Chrome + Xvfb）
├── docker-compose.yml             # Docker Compose 配置
├── pyproject.toml                 # Python 项目配置（uv）
├── uv.lock                        # 依赖锁文件
├── requirements.txt               # Python 依赖（兼容 pip）
├── README.md                      # 项目文档
├── .env.example                   # 环境变量配置示例
└── accounts_config.example.json   # 多账户配置示例
```

**运行时生成的文件和目录**:
- `accounts.json` - 账户配置持久化文件（Web编辑后保存）
- `data/stats.json` - 统计数据（访问量、请求数等）
- `data/images/` - 生成的图片存储目录
  - HF Pro: `/data/images`（持久化，重启不丢失）
  - 其他环境: `./data/images`（临时存储，重启会丢失）

**日志系统**:
- 内存日志缓冲区：最多保存 3000 条日志
- 自动淘汰机制：超过上限自动删除最旧的日志（FIFO）
- 重启后清空：日志存储在内存中，重启后丢失
- 内存占用：约 450KB - 750KB（非常小，不会爆炸）

## 🛠️ 技术栈

- **Python 3.11+**
- **FastAPI** - 现代Web框架
- **Uvicorn** - ASGI服务器
- **httpx** - HTTP客户端
- **Docker** - 容器化部署

## 📝 License

MIT License - 查看 [LICENSE](LICENSE) 文件了解详情

---

## 🙏 致谢

* 源项目：[F佬 Linux.do 讨论](https://linux.do/t/topic/1225645)
* 源项目：[heixxin/gemini](https://huggingface.co/spaces/heixxin/gemini/tree/main) | [Linux.do 讨论](https://linux.do/t/topic/1226413)
* 绘图参考：[Gemini-Link-System](https://github.com/qxd-ljy/Gemini-Link-System) | [Linux.do 讨论](https://linux.do/t/topic/1234363)
* Gemini Business 2API Helper 参考：[Linux.do 讨论](https://linux.do/t/topic/1231008)

---

## ⭐ Star History

[![Star History Chart](https://api.star-history.com/svg?repos=Dreamy-rain/gemini-business2api&type=date&legend=top-left)](https://www.star-history.com/#Dreamy-rain/gemini-business2api&type=date&legend=top-left)

---

**如果这个项目对你有帮助，请给个 ⭐ Star!**
