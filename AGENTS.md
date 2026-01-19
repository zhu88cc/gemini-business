# Repository Guidelines

## 项目结构与模块组织
- `main.py` 是 FastAPI 入口，负责路由、鉴权与启动逻辑。
- `core/` 存放核心服务（认证、账户、配置、Google API 适配、登录/注册服务）。
- `util/` 为通用工具（流式解析、模板辅助函数）。
- `templates/` 为 Jinja2 模板（`admin/`、`auth/`、`public/`、`components/`）。
- `static/` 为前端资源（`static/css`、`static/js`）。
- `data/` 为运行时数据（账户、统计、生成图片），多数已加入忽略。
- `docs/` 为文档，`script/` 为辅助脚本。

## 构建、测试与开发命令
- `pip install -r requirements.txt` 安装本地依赖。
- `cp .env.example .env` 初始化环境配置。
- `python main.py` 启动服务，地址 `http://localhost:7860`。
- `uvicorn main:app --reload --port 7860` 以热更新模式启动开发服务。
- `docker compose up --build` 构建并运行容器（挂载 `./data`）。

## 编码风格与命名规范
- Python 使用 4 空格缩进，函数/变量用 `snake_case`，类用 `PascalCase`，常量用 `UPPER_CASE`。
- 模块与模板文件名保持小写，必要时用下划线分隔。
- Jinja2 模板与 `static/js` 通过 DOM ID 强关联，改一处需同步另一处。
- JavaScript 采用 `camelCase` 命名，统一使用 `const`/`let`。

## 测试指南
- 当前仓库未配置自动化测试框架。
- 修改后至少进行冒烟测试：启动服务并验证 `/v1/models` 或后台页面可访问。
- 如需新增测试，建议使用 `pytest` 并放在 `tests/` 目录，补充运行方式说明。

## 提交与 PR 规范
- 提交信息使用类型前缀（如 `feat:`、`fix:`、`docs:`），后接简洁描述。
- PR 需包含变更说明、手动测试记录，以及必要的配置变更说明。
- 涉及 `templates/` 或 `static/` 的 UI 改动请附截图。

## 配置与数据文件
- 以 `.env.example` 为基准，本地配置放在 `.env`。
- 不要提交运行时数据（`data/` 与 `accounts.json` 已被忽略）。
