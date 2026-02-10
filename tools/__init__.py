"""
Tools模块 (Tools Module)

提供Agent可调用的工具函数
"""

from .knowledge_base import query_knowledge_base, register_knowledge_base_tool

__all__ = [
    'query_knowledge_base',
    'register_knowledge_base_tool'
]
