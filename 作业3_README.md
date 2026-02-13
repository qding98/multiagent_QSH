# 多智能体协作系统 (Multi-Agent Collaboration System)

<div align="center">

**基于 PyAutoGen 框架的智能多智能体协作系统**

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/downloads/)
[![Framework](https://img.shields.io/badge/framework-PyAutoGen-orange.svg)](https://github.com/microsoft/autogen)

</div>

## 📖 项目简介

这是一个基于微软 PyAutoGen 框架开发的多智能体协作系统，结合了 DeepSeek API 和 ChromaDB 向量数据库，实现了代码生成、多模态输出和 RAG（检索增强生成）知识库问答等功能。

本项目采用高度模块化的架构设计，将功能拆分为配置、RAG系统、智能体、工具函数、任务执行和工具类六大模块，代码结构清晰，易于维护和扩展。

### ✨ 核心功能

- **🤖 智能代码生成**: 基于自然语言描述自动生成 Python 代码
- **📊 数据可视化**: 使用 matplotlib 自动生成数据可视化图表
- **🔍 RAG 知识库问答**: 基于向量检索的智能问答系统
- **🧩 模块化架构**: 清晰的模块划分，易于扩展和维护
- **⚡ 异步执行**: 支持 async/await 异步编程模式
- **🚀 性能优化**: RAG系统批量处理，速度提升3-5倍
- **💾 本地部署**: 支持本地运行，无需 Docker

## 🛠️ 技术栈

| 技术 | 说明 |
|------|------|
| **框架** | PyAutoGen - 微软开源的多智能体框架 |
| **LLM** | DeepSeek API (deepseek-chat) |
| **向量数据库** | ChromaDB (本地持久化存储) |
| **Embedding** | sentence-transformers (all-MiniLM-L6-v2) |
| **可视化** | matplotlib |
| **运行环境** | Python 3.8+, Windows/Linux/macOS |

## 📁 项目结构

```
multiagent_QSH/
├── config/              # 配置模块
│   ├── __init__.py
│   └── llm_config.py   # LLM和API配置
├── rag/                 # RAG系统模块
│   ├── __init__.py
│   ├── rag_system.py   # RAG核心类（原始版本）
│   ├── rag_system_optimized.py  # RAG优化版本（批量处理）
│   └── initializer.py  # RAG初始化器
├── agents/              # Agent定义模块
│   ├── __init__.py
│   └── agent_factory.py # Agent创建工厂
├── tools/               # 工具函数模块
│   ├── __init__.py
│   └── knowledge_base.py # 知识库查询工具
├── tasks/               # 任务执行模块
│   ├── __init__.py
│   ├── fibonacci_task.py # 斐波那契任务（异步）
│   └── qa_task.py       # 问答任务（异步）
├── utils/               # 工具类模块
│   ├── __init__.py
│   └── logger.py        # 日志工具
├── main.py              # 主程序入口（异步）
├── requirements.txt     # 项目依赖
├── qsh_profile.txt      # 知识库文件
├── workspace/           # 代码执行工作目录
│   ├── fibonacci_qsh.png  # 生成的图表
│   ├── fibonacci_original.py  # Assistant原始代码
│   └── fibonacci_fixed.py     # 修复版本代码
├── chroma_db/           # 向量数据库存储目录
└── 性能优化说明.md      # 性能优化文档
```

### 模块说明

- **config/**: 管理所有配置项，支持环境变量和代码配置两种方式
- **rag/**: RAG系统核心，实现向量检索和文档管理
  - `rag_system.py`: 原始版本
  - `rag_system_optimized.py`: 优化版本（批量处理，性能提升3-5倍）
- **agents/**: Agent创建和管理，封装Assistant和UserProxy的配置逻辑
- **tools/**: Agent可调用的工具函数，如知识库查询工具
- **tasks/**: 任务执行逻辑，支持异步执行
- **utils/**: 通用工具函数，如日志输出工具
- **main.py**: 主程序入口（异步版本），协调各模块执行完整工作流

## 🚀 快速开始

### 环境要求

- Python 3.8 或更高版本
- pip 包管理器

### 安装步骤

1. **克隆项目**

```bash
git clone <repository-url>
cd multiagent_QSH
```

2. **安装依赖**

```bash
pip install -r requirements.txt
```

3. **配置 API Key**

选择以下任一方式配置 DeepSeek API Key：

**方式1：环境变量（推荐）**
```bash
# Linux/macOS
export DEEPSEEK_API_KEY="your-api-key-here"

# Windows (PowerShell)
$env:DEEPSEEK_API_KEY="your-api-key-here"

# Windows (CMD)
set DEEPSEEK_API_KEY=your-api-key-here
```

**方式2：代码配置**

编辑 `config/llm_config.py` 文件，修改第 17 行：
```python
DEEPSEEK_API_KEY = "your-api-key-here"
```

4. **运行程序**

```bash
python main.py
```

## 💡 使用示例

### 阶段一：代码生成与可视化

系统会自动执行斐波那契数列计算任务：
- 计算斐波那契数列前 20 项
- 使用 matplotlib 生成可视化图表
- 保存为 `workspace/fibonacci_qsh.png`

### 阶段二：RAG 知识库问答

系统会自动执行知识库问答任务：
- 初始化 RAG 系统，将 `qsh_profile.txt` 向量化
- 调用知识库查询工具检索相关信息
- 基于检索结果回答问题

### 自定义任务

你可以在 `tasks/` 目录下创建新的任务模块：

```python
# tasks/custom_task.py
async def run_custom_task(assistant, user_proxy):
    """
    自定义任务函数（异步版本）
    """
    task_message = """
    你的任务描述...
    """

    await user_proxy.a_initiate_chat(
        assistant,
        message=task_message,
        clear_history=True,
    )
```

然后在 `main.py` 中调用：

```python
from tasks import run_custom_task

# 在 async def main() 函数中添加
await run_custom_task(assistant, user_proxy)
```

## 🔧 配置说明

### LLM 配置

在 `config/llm_config.py` 中可以调整以下参数：

```python
llm_config = {
    "config_list": [
        {
            "model": "deepseek-chat",           # 模型名称
            "api_key": DEEPSEEK_API_KEY,        # API密钥
            "base_url": "https://api.deepseek.com",  # API基础URL
        }
    ],
    "temperature": 0.7,  # 温度参数（0-1），控制生成的随机性
    "timeout": 120,      # 超时时间（秒）
}
```

### RAG 配置

在 `rag/rag_system_optimized.py` 中可以调整：
- **Embedding 模型**: 默认使用 `all-MiniLM-L6-v2`
- **批处理大小**: `batch_size` 参数（默认32，可根据内存调整）
- **检索结果数量**: `n_results` 参数
- **向量数据库路径**: `db_path` 参数

**性能优化**：
- 原始版本：逐个处理文档，10个段落约2-3秒
- 优化版本：批量处理文档，10个段落约0.5-1秒
- **性能提升**: 3-5倍

详见 [性能优化说明.md](性能优化说明.md)

## 📚 开发指南

### 添加新功能

遵循以下步骤添加新功能：

1. **确定模块归属**
   - 配置相关 → `config/`
   - RAG相关 → `rag/`
   - Agent相关 → `agents/`
   - 工具函数 → `tools/`
   - 任务逻辑 → `tasks/`
   - 通用工具 → `utils/`

2. **创建新文件**：在对应模块下创建新的 Python 文件

3. **更新 `__init__.py`**：在模块的 `__init__.py` 中导出新功能

4. **更新 `main.py`**：如果需要，在主程序中调用新功能

### 代码规范

- **模块化**: 严禁将所有代码写在单一文件中
- **单一职责**: 每个模块只负责一个明确的功能领域
- **中文注释**: 所有代码必须包含详细的中文注释和 Docstring
- **依赖注入**: 通过参数传递依赖，避免全局变量

## ❓ 常见问题

### Q1: 如何获取 DeepSeek API Key？

访问 [DeepSeek 官网](https://www.deepseek.com/) 注册账号并获取 API Key。

### Q2: 为什么 RAG 系统初始化失败？

请确保 `qsh_profile.txt` 文件存在于项目根目录。

### Q3: 如何更换其他 LLM 模型？

修改 `config/llm_config.py` 中的 `model`、`api_key` 和 `base_url` 参数即可。

### Q4: 代码执行失败怎么办？

检查 `workspace/` 目录是否有写入权限，确保 Python 环境正确安装了所有依赖。

### Q6: 图片生成失败怎么办？

确保使用非交互式后端：
```python
import matplotlib
matplotlib.use('Agg')  # 在导入pyplot之前设置
```

参考 `workspace/fibonacci_fixed.py` 中的修复方案。

### Q7: 如何提升RAG系统性能？

项目已使用优化版本（`RAGSystemOptimized`），可以通过调整 `batch_size` 参数进一步优化：
```python
init_rag_system(knowledge_file="qsh_profile.txt", batch_size=64)  # 增大批处理
```

## 📝 更新日志

### v1.1.0 (2026-02-10)
- ✨ **异步化改造**: 全面支持 async/await 异步编程
- 🚀 **性能优化**: RAG系统批量处理，速度提升3-5倍
- 🔧 **图片生成修复**: 解决matplotlib在非交互环境中的问题
- 📦 **新增文件**:
  - `rag/rag_system_optimized.py` - RAG优化版本
  - `workspace/fibonacci_fixed.py` - 修复版本代码
  - `性能优化说明.md` - 详细的性能优化文档
- 📚 **文档完善**: 更新README和项目规范

### v1.0.0 (2026-02-09)
- ✨ 项目重构为模块化架构
- 🎯 拆分为 6 个功能模块
- 📦 完善项目文档和配置
- 🔧 优化代码结构和依赖管理

## 👤 作者

**QSH**

- 项目：机智小组大模型作业3
- 邮箱：[qushanhan@gmail.com]

---
