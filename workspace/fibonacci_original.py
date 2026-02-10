"""
斐波那契数列计算与可视化 - Assistant生成的原始代码
"""

import matplotlib.pyplot as plt
import numpy as np

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
# 设置中文字体支持
plt.rcParams['font.sans-serif'] = ['SimHei', 'Arial Unicode MS', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False

# 创建图形
plt.figure(figsize=(12, 6))

# 绘制折线图
x = list(range(1, n + 1))  # 项数：1到20
plt.plot(x, fib_numbers, 'b-o', linewidth=2, markersize=6, markerfacecolor='red')

# 设置图表属性
plt.title('斐波那契数列前20项 (QSH)', fontsize=16, fontweight='bold')
plt.xlabel('项数', fontsize=12)
plt.ylabel('数值', fontsize=12)

# 添加网格线
plt.grid(True, linestyle='--', alpha=0.7)

# 设置x轴刻度
plt.xticks(range(1, n + 1, 2))  # 每隔2项显示一个刻度

# 添加数值标签
for i, num in enumerate(fib_numbers, 1):
    plt.text(i, num, str(num), ha='center', va='bottom', fontsize=8)

# 调整布局
plt.tight_layout()

# 保存图表
plt.savefig('fibonacci_qsh.png', dpi=300, bbox_inches='tight')
print(f"\n图表已保存为: fibonacci_qsh.png")

# 显示图表
plt.show()

# 3. 输出统计信息
print(f"\n统计信息：")
print(f"最大值: {max(fib_numbers)} (第{n}项)")
print(f"最小值: {min(fib_numbers)} (第1项)")
print(f"平均值: {np.mean(fib_numbers):.2f}")
print(f"总和: {sum(fib_numbers)}")

# 计算相邻项的比例（黄金比例近似）
if n >= 3:
    print(f"\n相邻项比例（黄金比例近似）：")
    for i in range(2, n):
        ratio = fib_numbers[i] / fib_numbers[i-1] if fib_numbers[i-1] != 0 else 0
        print(f"第{i+1}项/第{i}项: {ratio:.6f}")
