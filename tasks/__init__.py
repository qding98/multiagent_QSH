"""
Tasks模块 (Tasks Module)

提供各类任务的执行逻辑
"""

from .fibonacci_task import run_fibonacci_task
from .qa_task import run_qa_task

__all__ = [
    'run_fibonacci_task',
    'run_qa_task'
]
