"""
日志工具模块 (Logger Utility Module)

提供格式化的日志输出功能
"""


def print_header(title: str, width: int = 60):
    """
    打印标题头部

    Args:
        title: 标题文本
        width: 宽度，默认为60
    """
    print("\n" + "=" * width)
    print(title)
    print("=" * width)


def print_section(title: str, width: int = 60):
    """
    打印章节标题

    Args:
        title: 章节标题
        width: 宽度，默认为60
    """
    print("\n" + "-" * width)
    print(title)
    print("-" * width)


def print_success(message: str):
    """
    打印成功消息

    Args:
        message: 消息内容
    """
    print(f"\n[成功] {message}")


def print_warning(message: str):
    """
    打印警告消息

    Args:
        message: 消息内容
    """
    print(f"\n[警告] {message}")


def print_error(message: str):
    """
    打印错误消息

    Args:
        message: 消息内容
    """
    print(f"\n[错误] {message}")
