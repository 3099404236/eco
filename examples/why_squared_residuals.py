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

# 创建可视化 - 使用3x2布局
fig = plt.figure(figsize=(16, 18))
gs = fig.add_gridspec(3, 2, hspace=0.3, wspace=0.3)

# 图1: OLS vs LAD 方法对比（正常的方法）
ax1 = fig.add_subplot(gs[0, 0])
ax1.scatter(X, Y, color='darkblue', s=80, alpha=0.7, label='Normal data',
           edgecolors='black', linewidth=0.5, zorder=3)
ax1.scatter(X[outlier_indices], Y[outlier_indices], color='crimson', s=150,
           marker='*', linewidth=1, label='Outliers', edgecolors='darkred', zorder=4)

x_line = np.linspace(X.min(), X.max(), 100)
ax1.plot(x_line, intercept_squared + slope_squared * x_line,
         color='navy', linewidth=3, label=f'OLS: Y={intercept_squared:.1f}+{slope_squared:.1f}X', zorder=2)
ax1.plot(x_line, intercept_abs + slope_abs * x_line,
         color='orangered', linewidth=3, linestyle='--',
         label=f'LAD: Y={intercept_abs:.1f}+{slope_abs:.1f}X', zorder=2)
ax1.plot(x_line, true_intercept + true_slope * x_line,
         color='green', linewidth=2, linestyle=':', alpha=0.8,
         label=f'True: Y={true_intercept}+{true_slope}X', zorder=1)

ax1.set_xlabel('X', fontsize=13, fontweight='bold')
ax1.set_ylabel('Y', fontsize=13, fontweight='bold')
ax1.set_title('Good Methods: OLS vs LAD', fontsize=15, fontweight='bold', pad=15)
ax1.legend(loc='upper left', fontsize=11, framealpha=0.95)
ax1.grid(True, alpha=0.3, linestyle='--')
ax1.set_facecolor('#f8f9fa')

# 图2: 为什么"残差和"方法失败（单独展示避免尺度问题）
ax2 = fig.add_subplot(gs[0, 1])
# 只显示"残差和"方法，用文字说明问题
ax2.text(0.5, 0.7, 'Why "Sum of Residuals" Fails', transform=ax2.transAxes,
        fontsize=18, fontweight='bold', ha='center', va='center',
        bbox=dict(boxstyle='round', facecolor='#ffe6e6', alpha=0.9, edgecolor='red', linewidth=3))
ax2.text(0.5, 0.45, f'Found: Y = {intercept_sum:.1e} + {slope_sum:.1e}X',
        transform=ax2.transAxes, fontsize=13, ha='center', va='center',
        family='monospace', color='darkred')
ax2.text(0.5, 0.30, f'Sum of residuals ≈ 0  (looks perfect!)',
        transform=ax2.transAxes, fontsize=12, ha='center', va='center',
        bbox=dict(boxstyle='round', facecolor='yellow', alpha=0.7))
ax2.text(0.5, 0.15, f'But... RSS = {np.sum(residuals_sum**2):.2e}  (terrible!)',
        transform=ax2.transAxes, fontsize=12, ha='center', va='center',
        bbox=dict(boxstyle='round', facecolor='lightcoral', alpha=0.7))
ax2.text(0.5, 0.02, 'Positive & negative errors cancel out!\nThis is why we SQUARE residuals.',
        transform=ax2.transAxes, fontsize=11, ha='center', va='bottom',
        style='italic', color='#cc0000', fontweight='bold')
ax2.axis('off')

# 图3: OLS残差可视化
ax3 = fig.add_subplot(gs[1, 0])
# 添加正负残差的可视化
for i, (x, r) in enumerate(zip(X, residuals_squared)):
    color = '#2ecc71' if r > 0 else '#e74c3c'
    ax3.vlines(x, 0, r, colors=color, alpha=0.7, linewidth=3, zorder=1)

ax3.scatter(X, residuals_squared, color='navy', s=60, alpha=0.8,
           edgecolors='black', linewidth=0.5, zorder=3)
ax3.scatter(X[outlier_indices], residuals_squared[outlier_indices],
           color='crimson', s=150, marker='*', linewidth=1,
           edgecolors='darkred', zorder=4)

ax3.axhline(y=0, color='black', linestyle='-', linewidth=2, zorder=2)
ax3.set_xlabel('X', fontsize=13, fontweight='bold')
ax3.set_ylabel('Residuals (e)', fontsize=13, fontweight='bold')
ax3.set_title(f'OLS Residuals Distribution (Σe = {np.sum(residuals_squared):.2f})',
             fontsize=15, fontweight='bold', pad=15)
ax3.grid(True, alpha=0.3, linestyle='--')
ax3.set_facecolor('#f8f9fa')

# 添加图例
from matplotlib.patches import Patch
legend_elements = [Patch(facecolor='#2ecc71', alpha=0.7, label='Positive errors'),
                   Patch(facecolor='#e74c3c', alpha=0.7, label='Negative errors')]
ax3.legend(handles=legend_elements, loc='upper right', fontsize=10)

# 图4: 经典例子 - 为什么不能直接求和
ax4 = fig.add_subplot(gs[1, 1])
example_X = np.array([1, 2])
example_Y_true = np.array([100000, 100000])
example_Y_pred_bad = np.array([1100000, -900000])
example_residuals = example_Y_true - example_Y_pred_bad

bar_positions = [0, 1]
colors_bar = ['#2ecc71' if r > 0 else '#e74c3c' for r in example_residuals]
bars = ax4.bar(bar_positions, example_residuals, color=colors_bar, alpha=0.8,
               edgecolor='black', linewidth=2.5, width=0.6)

ax4.axhline(y=0, color='black', linestyle='-', linewidth=2.5)
ax4.set_xlabel('Observation', fontsize=13, fontweight='bold')
ax4.set_ylabel('Residual Value', fontsize=13, fontweight='bold')
ax4.set_title('Classic Example: Why NOT Direct Sum?', fontsize=15, fontweight='bold', pad=15)
ax4.set_xticks([0, 1])
ax4.set_xticklabels(['Obs #1', 'Obs #2'], fontsize=12)
ax4.grid(True, alpha=0.3, axis='y', linestyle='--')
ax4.set_facecolor('#f8f9fa')

# 添加数值标签
for i, (pos, val) in enumerate(zip(bar_positions, example_residuals)):
    ax4.text(pos, val, f'{val:+,.0f}', ha='center',
            va='bottom' if val > 0 else 'top', fontsize=12, fontweight='bold',
            bbox=dict(boxstyle='round', facecolor='white', alpha=0.8, edgecolor='black'))

# 添加求和结果
sum_text = f'Σe = {example_residuals[0]:+,.0f} + {example_residuals[1]:+,.0f} = {np.sum(example_residuals):,.0f}'
squared_sum_text = f'Σe² = {example_residuals[0]**2:,.0f} + {example_residuals[1]**2:,.0f} = {np.sum(example_residuals**2):,.0f}'
ax4.text(0.5, 0.15, sum_text, transform=ax4.transAxes,
        fontsize=12, ha='center', va='center', fontweight='bold',
        bbox=dict(boxstyle='round', facecolor='#fff9c4', alpha=0.9, edgecolor='orange', linewidth=2))
ax4.text(0.5, 0.05, squared_sum_text, transform=ax4.transAxes,
        fontsize=12, ha='center', va='center', fontweight='bold',
        bbox=dict(boxstyle='round', facecolor='#b3e5fc', alpha=0.9, edgecolor='blue', linewidth=2))

# 图5: 残差 vs 残差平方对比
ax5 = fig.add_subplot(gs[2, 0])
n_show = 12
indices = np.arange(n_show)
width = 0.35

ax5.bar(indices - width/2, residuals_squared[:n_show], width,
       label='Residual (e)', alpha=0.8, color='#3498db', edgecolor='black', linewidth=1)
ax5.bar(indices + width/2, residuals_squared[:n_show]**2, width,
       label='Squared (e²)', alpha=0.8, color='#e74c3c', edgecolor='black', linewidth=1)

ax5.set_xlabel('Observation Number', fontsize=13, fontweight='bold')
ax5.set_ylabel('Value', fontsize=13, fontweight='bold')
ax5.set_title(f'First {n_show} Obs: Residuals vs Squared Residuals', fontsize=15, fontweight='bold', pad=15)
ax5.legend(fontsize=11, loc='upper right', framealpha=0.95)
ax5.grid(True, alpha=0.3, axis='y', linestyle='--')
ax5.axhline(y=0, color='black', linestyle='-', linewidth=1.5)
ax5.set_facecolor('#f8f9fa')
ax5.set_xticks(indices)

# 图6: 惩罚机制可视化
ax6 = fig.add_subplot(gs[2, 1])
error_range = np.linspace(-20, 20, 200)
squared_errors = error_range**2
absolute_errors = np.abs(error_range)

ax6.plot(error_range, squared_errors, color='#e74c3c', linewidth=3,
        label='Squared: e²', zorder=2)
ax6.plot(error_range, absolute_errors, color='#3498db', linewidth=3,
        linestyle='--', label='Absolute: |e|', zorder=2)

ax6.fill_between(error_range, 0, squared_errors, alpha=0.2, color='#e74c3c')
ax6.axvline(x=0, color='black', linestyle='-', linewidth=1.5, alpha=0.5)
ax6.axhline(y=0, color='black', linestyle='-', linewidth=1.5, alpha=0.5)

ax6.set_xlabel('Error Size (e)', fontsize=13, fontweight='bold')
ax6.set_ylabel('Penalty', fontsize=13, fontweight='bold')
ax6.set_title('Penalty Functions: How Errors Are Punished', fontsize=15, fontweight='bold', pad=15)
ax6.legend(fontsize=11, loc='upper center', framealpha=0.95)
ax6.grid(True, alpha=0.3, linestyle='--')
ax6.set_facecolor('#f8f9fa')

# 添加注释说明
ax6.annotate('Large errors get\nheavy penalty!', xy=(15, 225), xytext=(10, 300),
            fontsize=11, ha='center', fontweight='bold', color='#c0392b',
            arrowprops=dict(arrowstyle='->', color='#c0392b', lw=2),
            bbox=dict(boxstyle='round', facecolor='#ffe6e6', alpha=0.8))

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
