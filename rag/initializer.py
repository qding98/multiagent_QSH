"""
RAG系统初始化器 (RAG System Initializer)

提供RAG系统的全局实例管理和初始化功能
"""

import os
from .rag_system_optimized import RAGSystemOptimized  # 使用优化版本

# 全局 RAG 系统实例（单例模式）
_rag_instance = None


def init_rag_system(knowledge_file: str = "qsh_profile.txt", force_reload: bool = True, batch_size: int = 32) -> RAGSystemOptimized:
    """
    初始化全局 RAG 系统并加载知识库文档（使用优化版本）

    Args:
        knowledge_file: 知识库文件路径，默认为 "qsh_profile.txt"
        force_reload: 是否强制重新加载（清空旧数据），默认为 True
        batch_size: 批处理大小，默认为32（根据内存调整）

    Returns:
        RAGSystemOptimized: 初始化完成的 RAG 系统实例（优化版本）

    Raises:
        FileNotFoundError: 如果知识库文件不存在
    """
    global _rag_instance

    print("\n" + "-" * 60)
    print("初始化 RAG 知识库系统（优化版本）")
    print("-" * 60)

    # 检查知识库文件是否存在
    if not os.path.exists(knowledge_file):
        raise FileNotFoundError(f"知识库文件 {knowledge_file} 不存在！")

    # 初始化 RAG 系统（优化版本）
    _rag_instance = RAGSystemOptimized()

    # 如果需要强制重新加载，清空旧数据
    if force_reload:
        _rag_instance.clear_collection()

    # 加载知识库文档（使用批量处理）
    _rag_instance.add_document(knowledge_file, batch_size=batch_size)

    print(f"[RAG] 知识库初始化完成，共 {_rag_instance.get_collection_count()} 条记录")
    print("-" * 60)

    return _rag_instance


def get_rag_instance() -> RAGSystemOptimized:
    """
    获取全局 RAG 系统实例

    Returns:
        RAGSystemOptimized: RAG 系统实例（优化版本）

    Raises:
        RuntimeError: 如果 RAG 系统尚未初始化
    """
    global _rag_instance

    if _rag_instance is None:
        raise RuntimeError("RAG 系统尚未初始化，请先调用 init_rag_system()")

    return _rag_instance
