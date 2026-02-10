"""
问答任务模块 (Q&A Task Module)

实现基于RAG的知识库问答任务
"""


async def run_qa_task(assistant, user_proxy):
    """
    执行RAG知识库问答任务（异步版本）

    任务流程：
    1. 系统已初始化 RAG（在 main 函数中完成）
    2. UserProxy 提问关于 QSH 的问题
    3. Assistant 调用 query_knowledge_base 工具检索信息
    4. Assistant 基于检索结果回答问题

    Args:
        assistant: AssistantAgent 实例
        user_proxy: UserProxyAgent 实例
    """
    print("\n" + "=" * 60)
    print("阶段二：RAG 知识库问答")
    print("任务：使用 RAG 系统回答关于 QSH 的问题")
    print("=" * 60 + "\n")

    # 定义问答任务
    qa_message = """
请回答以下问题：

QSH 的电脑配置怎么样？他喜欢什么运动？

注意：你需要调用 query_knowledge_base 工具来获取相关信息，然后基于检索到的内容回答。
不要编造信息，只使用从知识库中检索到的内容。

回答完成后请回复 TERMINATE。
"""

    # 发起对话（异步调用）
    await user_proxy.a_initiate_chat(
        assistant,
        message=qa_message,
        clear_history=True,
    )
