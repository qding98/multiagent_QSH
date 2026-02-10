"""
斐波那契任务模块 (Fibonacci Task Module)

实现斐波那契数列计算与可视化任务
"""

import os


async def run_fibonacci_task(assistant, user_proxy, output_dir: str = "workspace"):
    """
    执行斐波那契数列计算与可视化任务（异步版本）

    任务流程：
    1. UserProxy 发布任务：计算斐波那契数列前 20 项
    2. Assistant 编写计算代码
    3. Assistant 编写 matplotlib 可视化代码
    4. UserProxy 执行代码并生成图片

    Args:
        assistant: AssistantAgent 实例
        user_proxy: UserProxyAgent 实例
        output_dir: 输出目录，默认为 "workspace"
    """
    print("\n" + "=" * 60)
    print("阶段一：代码生成与多模态输出")
    print("任务：计算斐波那契数列前 20 项并生成可视化图表")
    print("=" * 60 + "\n")

    # 定义任务消息
    task_message = """
请完成以下任务：

1. 编写 Python 代码计算斐波那契数列的前 20 项
2. 使用 matplotlib 将这 20 项数据绘制成折线图
3. 图表要求：
   - 标题：斐波那契数列前20项 (QSH)
   - X轴标签：项数
   - Y轴标签：数值
   - 显示网格线
   - 保存为 fibonacci_qsh.png

请将所有代码写在一个代码块中执行。完成后回复 TERMINATE。
"""

    # 发起对话（异步调用）
    await user_proxy.a_initiate_chat(
        assistant,
        message=task_message,
        clear_history=True,
    )

    # 检查输出文件
    output_file = os.path.join(output_dir, "fibonacci_qsh.png")
    if os.path.exists(output_file):
        print(f"\n[成功] 图表已生成: {output_file}")
    else:
        print(f"\n[警告] 未找到输出文件: {output_file}")
