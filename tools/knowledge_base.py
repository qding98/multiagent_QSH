"""
知识库查询工具 (Knowledge Base Query Tool)

提供Agent可调用的知识库检索功能
"""

from typing import Annotated
from rag import get_rag_instance


def query_knowledge_base(question: Annotated[str, "要查询的问题"]) -> str:
    """
    查询知识库工具函数

    这是一个注册给 Agent 使用的工具函数，Agent 可以调用此函数来检索知识库中的信息

    Args:
        question: 用户提出的问题

    Returns:
        从知识库中检索到的相关信息
    """
    try:
        # 获取 RAG 系统实例
        rag_system = get_rag_instance()

        # 调用 RAG 系统进行检索
        context = rag_system.query(question, n_results=5)

        if not context:
            return "未在知识库中找到相关信息"

        return f"从知识库中检索到以下信息：\n{context}"

    except RuntimeError as e:
        return f"错误：{str(e)}"
    except Exception as e:
        return f"查询知识库时发生错误：{str(e)}"


def register_knowledge_base_tool(assistant, user_proxy):
    """
    将知识库查询工具注册到Agent

    Args:
        assistant: AssistantAgent 实例
        user_proxy: UserProxyAgent 实例
    """
    # 注册工具函数：让 Assistant 可以调用 RAG 查询
    assistant.register_for_llm(
        name="query_knowledge_base",
        description="查询知识库以获取关于 QSH 的个人信息，包括电脑配置、爱好、特长等"
    )(query_knowledge_base)

    user_proxy.register_for_execution(
        name="query_knowledge_base"
    )(query_knowledge_base)

    print("[Tools] 已注册工具函数: query_knowledge_base")
