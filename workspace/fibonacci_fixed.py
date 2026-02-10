"""
斐波那契数列计算与可视化 - 修复版本

修复内容：
1. 移除 plt.show()（避免在非交互环境中的问题）
2. 使用 Agg 后端（不需要显示窗口）
3. 确保保存到workspace目录
4. 简化中文字体设置
5. 添加更详细的错误处理
"""

import matplotlib
matplotlib.use('Agg')  # 使用非交互式后端
import matplotlib.pyplot as plt
import numpy as np
import os

# 确保在workspace目录中执行
output_dir = "workspace"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# 1. 计算斐波那契数列的前20项
def fibonacci(n):
    """计算斐波那契数列的前n项"""
    fib_sequence = [0, 1]  # 前两项

    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return fib_sequence

    # 计算后续项
    for i in range(2, n):
        next_value = fib_sequence[i-1] + fib_sequence[i-2]
        fib_sequence.append(next_value)

    return fib_sequence

# 计算前20项
n = 20
fib_numbers = fibonacci(n)
print(f"斐波那契数列前{n}项：")
for i, num in enumerate(fib_numbers, 1):
    print(f"第{i}项: {num}")

# 2. 使用matplotlib绘制折线图
try:
    # 设置中文字体支持（简化版本）
    plt.rcParams['font.sans-serif'] = ['SimHei', 'Microsoft YaHei', 'Arial Unicode MS', 'DejaVu Sans']
    plt.rcParams['axes.unicode_minus'] = False

    # 创建图形
    plt.figure(figsize=(12, 6))

    # 绘制折线图
    x = list(range(1, n + 1))  # 项数：1到20
    plt.plot(x, fib_numbers, 'b-o', linewidth=2, markersize=6, markerfacecolor='red')

    # 设置图表属性
    plt.title('Fibonacci Sequence (QSH)', fontsize=16, fontweight='bold')
    plt.xlabel('Index', fontsize=12)
    plt.ylabel('Value', fontsize=12)

    # 添加网格线
    plt.grid(True, linestyle='--', alpha=0.7)

    # 设置x轴刻度
    plt.xticks(range(1, n + 1, 2))  # 每隔2项显示一个刻度

    # 调整布局
    plt.tight_layout()

    # 保存图表到workspace目录
    output_path = os.path.join(output_dir, 'fibonacci_qsh.png')
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    print(f"\n[成功] 图表已保存为: {output_path}")

    # 验证文件是否存在
    if os.path.exists(output_path):
        file_size = os.path.getsize(output_path)
        print(f"[验证] 文件大小: {file_size} 字节")
    else:
        print(f"[错误] 文件未成功保存")

except Exception as e:
    print(f"[错误] 绘图过程中出现异常: {e}")
    import traceback
    traceback.print_exc()

# 3. 输出统计信息
print(f"\n统计信息：")
print(f"最大值: {max(fib_numbers)} (第{n}项)")
print(f"最小值: {min(fib_numbers)} (第1项)")
print(f"平均值: {np.mean(fib_numbers):.2f}")
print(f"总和: {sum(fib_numbers)}")

print("\n程序执行完成！")
