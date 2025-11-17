"""
为什么要平方残差？直观演示

这个脚本比较三种不同的残差最小化方法：
1. 最小化残差和 (Σeᵢ) - 有缺陷的方法
2. 最小化残差平方和 (Σeᵢ²) - OLS标准方法
3. 最小化残差绝对值和 (Σ|eᵢ|) - LAD方法
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize
import matplotlib
matplotlib.rcParams['font.sans-serif'] = ['SimHei', 'DejaVu Sans']  # 支持中文显示
matplotlib.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题

# 设置随机种子以保证结果可重现
np.random.seed(42)

# 生成样本数据
# 真实关系: Y = 10 + 2*X + 噪声
n_samples = 30
X = np.linspace(0, 10, n_samples)
true_intercept = 10
true_slope = 2
# 添加一些噪声，并特意加入几个离群点
noise = np.random.normal(0, 2, n_samples)
# 添加3个离群点
outlier_indices = [5, 15, 25]
noise[outlier_indices] = [15, -12, 18]
Y = true_intercept + true_slope * X + noise

def calculate_residuals(X, Y, intercept, slope):
    """计算残差"""
    Y_pred = intercept + slope * X
    residuals = Y - Y_pred
    return residuals, Y_pred

def sum_of_residuals(params, X, Y):
    """目标函数1: 残差和 (有问题的方法)"""
    intercept, slope = params
    residuals, _ = calculate_residuals(X, Y, intercept, slope)
    return np.sum(residuals)

def sum_of_squared_residuals(params, X, Y):
    """目标函数2: 残差平方和 (OLS)"""
    intercept, slope = params
    residuals, _ = calculate_residuals(X, Y, intercept, slope)
    return np.sum(residuals**2)

def sum_of_absolute_residuals(params, X, Y):
    """目标函数3: 残差绝对值和 (LAD)"""
    intercept, slope = params
    residuals, _ = calculate_residuals(X, Y, intercept, slope)
    return np.sum(np.abs(residuals))

# 初始猜测
initial_params = [0, 0]

# 方法1: 最小化残差和
print("=" * 60)
print("方法1: 最小化残差和 Σeᵢ")
print("=" * 60)
# 注意：这个优化会失败或给出荒谬的结果，因为可以通过极端的参数让正负误差抵消
result_sum = minimize(sum_of_residuals, initial_params, args=(X, Y), method='BFGS')
intercept_sum, slope_sum = result_sum.x
residuals_sum, Y_pred_sum = calculate_residuals(X, Y, intercept_sum, slope_sum)
print(f"拟合结果: Y = {intercept_sum:.2f} + {slope_sum:.2f}*X")
print(f"残差和: {np.sum(residuals_sum):.2f}")
print(f"残差平方和: {np.sum(residuals_sum**2):.2f}")
print(f"警告: 这个方法找到的直线可能非常糟糕！\n")

# 方法2: 最小化残差平方和 (OLS)
print("=" * 60)
print("方法2: 最小化残差平方和 Σeᵢ² (OLS标准方法)")
print("=" * 60)
result_squared = minimize(sum_of_squared_residuals, initial_params, args=(X, Y), method='BFGS')
intercept_squared, slope_squared = result_squared.x
residuals_squared, Y_pred_squared = calculate_residuals(X, Y, intercept_squared, slope_squared)
print(f"拟合结果: Y = {intercept_squared:.2f} + {slope_squared:.2f}*X")
print(f"残差和: {np.sum(residuals_squared):.2f}")
print(f"残差平方和: {np.sum(residuals_squared**2):.2f}")
print(f"真实参数: Y = {true_intercept:.2f} + {true_slope:.2f}*X\n")

# 方法3: 最小化残差绝对值和 (LAD)
print("=" * 60)
print("方法3: 最小化残差绝对值和 Σ|eᵢ| (LAD方法)")
print("=" * 60)
result_abs = minimize(sum_of_absolute_residuals, initial_params, args=(X, Y), method='Nelder-Mead')
intercept_abs, slope_abs = result_abs.x
residuals_abs, Y_pred_abs = calculate_residuals(X, Y, intercept_abs, slope_abs)
print(f"拟合结果: Y = {intercept_abs:.2f} + {slope_abs:.2f}*X")
print(f"残差绝对值和: {np.sum(np.abs(residuals_abs)):.2f}")
print(f"残差平方和: {np.sum(residuals_abs**2):.2f}")
print("注: LAD方法对离群点更稳健\n")

# 创建可视化
fig, axes = plt.subplots(2, 2, figsize=(15, 12))

# 图1: 三种方法的对比
ax1 = axes[0, 0]
ax1.scatter(X, Y, color='black', s=50, alpha=0.6, label='观测数据')
ax1.scatter(X[outlier_indices], Y[outlier_indices], color='red', s=100,
           marker='x', linewidth=3, label='离群点')

x_line = np.linspace(X.min(), X.max(), 100)
ax1.plot(x_line, intercept_sum + slope_sum * x_line, 'g--',
         linewidth=2, label=f'残差和: Y={intercept_sum:.1f}+{slope_sum:.1f}X')
ax1.plot(x_line, intercept_squared + slope_squared * x_line, 'b-',
         linewidth=2, label=f'残差平方和(OLS): Y={intercept_squared:.1f}+{slope_squared:.1f}X')
ax1.plot(x_line, intercept_abs + slope_abs * x_line, 'r-.',
         linewidth=2, label=f'残差绝对值和: Y={intercept_abs:.1f}+{slope_abs:.1f}X')
ax1.plot(x_line, true_intercept + true_slope * x_line, 'k:',
         linewidth=2, alpha=0.5, label=f'真实关系: Y={true_intercept}+{true_slope}X')

ax1.set_xlabel('X', fontsize=12)
ax1.set_ylabel('Y', fontsize=12)
ax1.set_title('三种拟合方法对比', fontsize=14, fontweight='bold')
ax1.legend(loc='best', fontsize=9)
ax1.grid(True, alpha=0.3)

# 图2: 残差可视化 (OLS方法)
ax2 = axes[0, 1]
ax2.scatter(X, residuals_squared, color='blue', s=50, alpha=0.6)
ax2.scatter(X[outlier_indices], residuals_squared[outlier_indices],
           color='red', s=100, marker='x', linewidth=3)
ax2.axhline(y=0, color='black', linestyle='-', linewidth=1)
ax2.set_xlabel('X', fontsize=12)
ax2.set_ylabel('残差 eᵢ', fontsize=12)
ax2.set_title(f'OLS残差分布 (Σeᵢ={np.sum(residuals_squared):.2f})',
             fontsize=14, fontweight='bold')
ax2.grid(True, alpha=0.3)

# 添加正负残差的可视化
for i, (x, r) in enumerate(zip(X, residuals_squared)):
    color = 'green' if r > 0 else 'orange'
    ax2.vlines(x, 0, r, colors=color, alpha=0.5, linewidth=2)

# 图3: 展示为什么不能直接求和
ax3 = axes[1, 0]
# 创建一个简单的例子，如用户描述的
example_X = np.array([1, 2])
example_Y_true = np.array([100000, 100000])
example_Y_pred_bad = np.array([1100000, -900000])
example_residuals = example_Y_true - example_Y_pred_bad

bar_positions = [0, 1]
colors = ['green' if r > 0 else 'red' for r in example_residuals]
bars = ax3.bar(bar_positions, example_residuals, color=colors, alpha=0.7,
               edgecolor='black', linewidth=2)

ax3.axhline(y=0, color='black', linestyle='-', linewidth=2)
ax3.set_xlabel('观测值编号', fontsize=12)
ax3.set_ylabel('残差值', fontsize=12)
ax3.set_title('为什么不能直接求和？示例', fontsize=14, fontweight='bold')
ax3.set_xticks([0, 1])
ax3.set_xticklabels(['观测1', '观测2'])
ax3.grid(True, alpha=0.3, axis='y')

# 添加数值标签
for i, (pos, val) in enumerate(zip(bar_positions, example_residuals)):
    ax3.text(pos, val, f'{val:+,.0f}', ha='center',
            va='bottom' if val > 0 else 'top', fontsize=10, fontweight='bold')

# 添加求和结果
sum_text = f'Σeᵢ = {example_residuals[0]:+,.0f} + {example_residuals[1]:+,.0f} = {np.sum(example_residuals):,.0f}'
squared_sum_text = f'Σeᵢ² = {example_residuals[0]**2:,.0f} + {example_residuals[1]**2:,.0f} = {np.sum(example_residuals**2):,.0f}'
ax3.text(0.5, 0.95, sum_text, transform=ax3.transAxes,
        fontsize=11, ha='center', va='top',
        bbox=dict(boxstyle='round', facecolor='yellow', alpha=0.7))
ax3.text(0.5, 0.85, squared_sum_text, transform=ax3.transAxes,
        fontsize=11, ha='center', va='top',
        bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.7))

# 图4: 残差平方和的可视化
ax4 = axes[1, 1]
# 显示残差和残差平方的对比
indices = np.arange(len(residuals_squared))
width = 0.35

# 只显示前10个点，避免太拥挤
n_show = 10
ax4.bar(indices[:n_show] - width/2, residuals_squared[:n_show], width,
       label='残差 eᵢ', alpha=0.7, color='blue')
ax4.bar(indices[:n_show] + width/2, residuals_squared[:n_show]**2, width,
       label='残差平方 eᵢ²', alpha=0.7, color='red')

ax4.set_xlabel('观测值编号', fontsize=12)
ax4.set_ylabel('值', fontsize=12)
ax4.set_title('前10个观测：残差 vs 残差平方', fontsize=14, fontweight='bold')
ax4.legend(fontsize=10)
ax4.grid(True, alpha=0.3, axis='y')
ax4.axhline(y=0, color='black', linestyle='-', linewidth=1)

plt.tight_layout()
plt.savefig('/home/user/eco/examples/why_squared_residuals.png', dpi=300, bbox_inches='tight')
print("=" * 60)
print(f"图表已保存到: /home/user/eco/examples/why_squared_residuals.png")
print("=" * 60)

# 额外分析：展示目标函数的形状
print("\n" + "=" * 60)
print("关键洞察：不同目标函数的特性")
print("=" * 60)
print(f"1. 残差和方法的问题：")
print(f"   - 正负残差可以相互抵消")
print(f"   - 残差和接近0并不意味着拟合好")
print(f"   - 在我们的例子中，残差和={np.sum(residuals_sum):.2f}，")
print(f"     但残差平方和={np.sum(residuals_sum**2):.2f}（很大！）")
print(f"\n2. 残差平方和方法(OLS)的优点：")
print(f"   - 正负残差都被平方，不会抵消")
print(f"   - 大的误差会被「惩罚」得更重（平方增长）")
print(f"   - 有唯一的解析解，计算高效")
print(f"   - 残差平方和={np.sum(residuals_squared**2):.2f}")
print(f"\n3. 残差绝对值和方法(LAD)的特点：")
print(f"   - 对离群点更稳健（不会过度惩罚大误差）")
print(f"   - 但计算上更复杂")
print(f"   - 残差绝对值和={np.sum(np.abs(residuals_abs)):.2f}")

plt.show()
