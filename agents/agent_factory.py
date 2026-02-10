"""
Agent工厂模块 (Agent Factory Module)

负责创建和配置多智能体系统中的各类Agent

Agent类型：
1. AssistantAgent: AI助手，负责代码生成、问题回答等
2. UserProxyAgent: 用户代理，负责代码执行和工具调用
"""

from autogen import AssistantAgent, UserProxyAgent
from config import get_llm_config


def create_assistant(llm_config: dict = None) -> AssistantAgent:
    """
    创建 Assistant Agent（AI 助手）

    Args:
        llm_config: LLM配置字典，如果为None则使用默认配置

    Returns:
        AssistantAgent: 配置完成的 Assistant Agent 实例
    """
    if llm_config is None:
        llm_config = get_llm_config()

    assistant = AssistantAgent(
        name="Assistant",
        system_message="""你是一个智能助手，擅长编写 Python 代码和回答问题。

你的能力包括：
1. 编写和执行 Python 代码来完成计算任务
2. 使用 matplotlib 创建数据可视化图表
3. 调用 query_knowledge_base 工��来检索知识库中的信息

当用户询问关于特定人物（如 QSH）的信息时，你必须先调用 query_knowledge_base 工具获取相关信息，然后基于检索结果回答。

请确保代码简洁、正确，并包含必要的中文注释。""",
        llm_config=llm_config,
    )

    print("[Agent] Assistant Agent 创建完成")
    return assistant


def create_user_proxy(work_dir: str = "workspace") -> UserProxyAgent:
    """
    创建 UserProxy Agent（用户代理）

    Args:
        work_dir: 代码执行工作目录，默认为 "workspace"

    Returns:
        UserProxyAgent: 配置完成的 UserProxy Agent 实例
    """
    user_proxy = UserProxyAgent(
        name="UserProxy",
        human_input_mode="NEVER",  # 自动模式，不需要人工输入
        max_consecutive_auto_reply=10,  # 最大连续自动回复次数
        is_termination_msg=lambda x: x.get("content", "").rstrip().endswith("TERMINATE"),
        code_execution_config={
            "work_dir": work_dir,  # 代码执行工作目录
            "use_docker": False,   # 不使用 Docker，本地执行
        },
    )

    print(f"[Agent] UserProxy Agent 创建完成 (工作目录: {work_dir})")
    return user_proxy


def create_agents(llm_config: dict = None, work_dir: str = "workspace") -> tuple:
    """
    创建多智能体系统中的所有 Agent

    Args:
        llm_config: LLM配置字典，如果为None则使用默认配置
        work_dir: 代码执行工作目录，默认为 "workspace"

    Returns:
        tuple: (assistant, user_proxy) Agent 实例元组
    """
    print("\n" + "=" * 60)
    print("正在创建 Agent...")
    print("=" * 60)

    # 创建 Assistant 和 UserProxy
    assistant = create_assistant(llm_config)
    user_proxy = create_user_proxy(work_dir)

    print("=" * 60)

    return assistant, user_proxy
