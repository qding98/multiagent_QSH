# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## 项目概述

这是一个基于微软 `pyautogen` 框架的多智能体协作系统（Multi-Agent Collaboration），用于深度学习课程大作业。

## 技术栈

- **框架**: pyautogen
- **LLM**: DeepSeek API（模型: `deepseek-chat`，Base URL: `https://api.deepseek.com`）
- **向量数据库**: ChromaDB（本地）
- **Embedding**: sentence-transformers (`all-MiniLM-L6-v2`)
- **运行环境**: 本地 Windows，不使用 Docker（`use_docker=False`）

## 常用命令

```bash
# 安装依赖
pip install -r requirements.txt

# 运行主程序
python main.py
```

## 项目结构

本项目采用模块化架构，按功能划分为以下模块：

```
multiagent_QSH/
├── config/              # 配置模块
│   ├── __init__.py
│   └── llm_config.py   # LLM和API配置
├── rag/                 # RAG系统模块
│   ├── __init__.py
│   ├── rag_system.py   # RAG核心类
│   └── initializer.py  # RAG初始化器
├── agents/              # Agent定义模块
│   ├── __init__.py
│   └── agent_factory.py # Agent创建工厂
├── tools/               # 工具函数模块
│   ├── __init__.py
│   └── knowledge_base.py # 知识库查询工具
├── tasks/               # 任务执行模块
│   ├── __init__.py
│   ├── fibonacci_task.py # 斐波那契任务
│   └── qa_task.py       # 问答任务
├── utils/               # 工具类模块
│   ├── __init__.py
│   └── logger.py        # 日志工具
├── main.py              # 主入口（简化版）
├── requirements.txt     # 依赖文件
├── qsh_profile.txt      # 知识库文件
├── workspace/           # 代码执行工作目录
└── chroma_db/           # 向量数据库存储目录
```

### 模块职责

1. **config/**: 管理所有配置项
   - `llm_config.py`: DeepSeek API配置、LLM参数配置
   - 支持环境变量和代码配置两种方式

2. **rag/**: RAG系统核心
   - `rag_system.py`: 实现向量检索、文档管理
   - `initializer.py`: 全局RAG实例管理（单例模式）

3. **agents/**: Agent创建和管理
   - `agent_factory.py`: 创建Assistant和UserProxy Agent
   - 封装Agent配置逻辑

4. **tools/**: Agent可调用的工具函数
   - `knowledge_base.py`: 知识库查询工具
   - 工具注册逻辑

5. **tasks/**: 任务执行逻辑
   - `fibonacci_task.py`: 斐波那契计算与可视化
   - `qa_task.py`: RAG问答任务

6. **utils/**: 通用工具函数
   - `logger.py`: 格式化日志输出

7. **main.py**: 主程序入口
   - 协调各模块，执行完整工作流

## 核心架构

### 工作流程

1. **阶段一：代码生成与多模态输出**
   - UserProxy 发布斐波那契计算任务
   - Assistant 生成计算代码和 matplotlib 可视化代码
   - 输出 `fibonacci_qsh.png` 图片

2. **阶段二：RAG 知识库问答**
   - 初始化 RAG：将 `qsh_profile.txt` 向量化存入 ChromaDB
   - 注册工具函数 `query_knowledge_base(question)`
   - Agent 调用 RAG 工具检索并回答问题

### 关键配置

- `llm_config`: 在 `config/llm_config.py` 中定义，包含 DeepSeek API 配置
- `api_key`: 支持环境变量 `DEEPSEEK_API_KEY` 或直接在代码中配置

### API Key 配置方式

**方式1：环境变量（推荐）**
```bash
export DEEPSEEK_API_KEY="your-api-key-here"
```

**方式2：代码配置**
在 `config/llm_config.py` 中修改 `DEEPSEEK_API_KEY` 变量

## RAG 知识库数据

知识库文件 `qsh_profile.txt` 包含以下个人信息：
- 姓名、身份、设备配置、特长、爱好、作业目标、年龄、生日、鞋码

## 开发规范

### 代码组织原则

1. **模块化**: 严禁将所有代码写在单一文件中，必须按功能模块拆分
2. **单一职责**: 每个模块只负责一个明确的功能领域
3. **依赖注入**: 通过参数传递依赖，避免全局变量（RAG实例除外，采用单例模式）
4. **中文注释**: 所有代码必须包含详细的中文注释和Docstring

### 添加新功能

当需要添加新功能时，请遵循以下步骤：

1. **确定模块归属**: 判断新功能属于哪个模块
   - 配置相关 → `config/`
   - RAG相关 → `rag/`
   - Agent相关 → `agents/`
   - 工具函数 → `tools/`
   - 任务逻辑 → `tasks/`
   - 通用工具 → `utils/`

2. **创建新文件**: 在对应模块下创建新的Python文件
3. **更新__init__.py**: 在模块的`__init__.py`中导出新功能
4. **更新main.py**: 如果需要，在主程序中调用新功能

### 示例：添加新任务

假设要添加一个"数据分析任务"：

1. 在 `tasks/` 目录下创建 `data_analysis_task.py`
2. 实现任务函数 `run_data_analysis_task(assistant, user_proxy)`
3. 在 `tasks/__init__.py` 中添加导出
4. 在 `main.py` 中调用新任务

## 更新日志

- **2026-02-09**: 项目重构为模块化架构，拆分为6个功能模块
