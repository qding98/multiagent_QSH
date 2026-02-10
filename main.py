"""
多智能体协作系统 - 主程序 (Multi-Agent Collaboration System - Main)

基于 PyAutoGen 框架实现，使用 DeepSeek API 作为 LLM 后端

功能：
1. 阶段一：代码生成与多模态输出（斐波那契数列计算与可视化）
2. 阶段二：RAG 知识库问答（基于 ChromaDB 向量数据库）

作者：QSH
课程：深度学习大作业

项目结构：
- config/: 配置模块（LLM配置、API配置）
- rag/: RAG系统模块（向量检索、知识库管理）
- agents/: Agent定义模块（Assistant、UserProxy）
- tools/: 工具函数模块（知识库查询工具）
- tasks/: 任务执行模块（斐波那契任务、问答任务）
- utils/: 工具类模块（日志工具）
"""

import os
import asyncio
from config import get_llm_config
from rag import init_rag_system
from agents import create_agents
from tools import register_knowledge_base_tool
from tasks import run_fibonacci_task, run_qa_task
from utils import print_header


async def main():
    """
    主函数 - 程序入口（异步版本）

    执行流程：
    1. 检查 API Key 配置
    2. 创建工作目录
    3. 初始化 RAG 系统
    4. 创建 Agent
    5. 注册工具函数
    6. 执行阶段一：代码生成与多模态输出
    7. 执行阶段二：RAG 知识库问答
    """
    # 打印欢迎信息
    print_header("多智能体协作系统 (Multi-Agent Collaboration System)")
    print("基于 PyAutoGen + DeepSeek API + ChromaDB")
    print("作者：QSH | 深度学习课程大作业")
    print("=" * 60)

    # 步骤2：创建工作目录（用于存放生成的代码和文件）
    work_dir = "workspace"
    os.makedirs(work_dir, exist_ok=True)
    print(f"\n[系统] 工作目录已创建: {work_dir}/")

    # 步骤3：初始化 RAG 系统
    try:
        init_rag_system(knowledge_file="qsh_profile.txt", force_reload=True)
    except FileNotFoundError as e:
        print(f"\n[错误] {e}")
        return
    except Exception as e:
        print(f"\n[错误] RAG系统初始化失败: {e}")
        return

    # 步骤4：创建 Agent
    llm_config = get_llm_config()
    assistant, user_proxy = create_agents(llm_config=llm_config, work_dir=work_dir)

    # 步骤5：注册工具函数
    register_knowledge_base_tool(assistant, user_proxy)

    # 步骤6：执行阶段一 - 代码生成与多模态输出（使用await）
    await run_fibonacci_task(assistant, user_proxy, output_dir=work_dir)

    # 步骤7：执行阶段二 - RAG 知识库问答（使用await）
    await run_qa_task(assistant, user_proxy)

    # 完成
    print_header("所有任务执行完成！")
    print("\n生成的文件：")
    print(f"  - {work_dir}/fibonacci_qsh.png (斐波那契数列可视化图表)")
    print("  - chroma_db/ (向量数据库存储目录)")
    print()


if __name__ == "__main__":
    asyncio.run(main())
