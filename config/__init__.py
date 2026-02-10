"""
配置模块 (Configuration Module)

提供LLM配置、API配置等全局配置项
"""

from .llm_config import (
    DEEPSEEK_API_KEY,
    DEEPSEEK_BASE_URL,
    DEEPSEEK_MODEL,
    llm_config,
    get_llm_config
)

__all__ = [
    'DEEPSEEK_API_KEY',
    'DEEPSEEK_BASE_URL',
    'DEEPSEEK_MODEL',
    'llm_config',
    'get_llm_config'
]
