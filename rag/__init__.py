"""
RAG模块 (Retrieval-Augmented Generation Module)

提供基于ChromaDB的向量检索和知识库管理功能
"""

from .rag_system import RAGSystem
from .rag_system_optimized import RAGSystemOptimized
from .initializer import init_rag_system, get_rag_instance

__all__ = [
    'RAGSystem',
    'RAGSystemOptimized',
    'init_rag_system',
    'get_rag_instance'
]
