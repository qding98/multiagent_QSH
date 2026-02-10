"""
Agents模块 (Agents Module)

提供多智能体系统中的Agent创建和管理功能
"""

from .agent_factory import create_agents, create_assistant, create_user_proxy

__all__ = [
    'create_agents',
    'create_assistant',
    'create_user_proxy'
]
