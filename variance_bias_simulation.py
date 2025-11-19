"""
蒙特卡洛模拟：证明样本方差除以(N-1)是无偏估计
纯Python实现，无需外部依赖
"""
import random
import math

# 设置随机种子以保证结果可重复
random.seed(42)

def generate_normal_sample(mu, sigma, n):
    """使用Box-Muller变换生成正态分布样本"""
    sample = []
    for _ in range(n):
        # Box-Muller变换
        u1 = random.random()
        u2 = random.random()
        z = math.sqrt(-2 * math.log(u1)) * math.cos(2 * math.pi * u2)
        x = mu + sigma * z
        sample.append(x)
    return sample

def calculate_mean(data):
    """计算均值"""
    return sum(data) / len(data)

def calculate_variance(data, sample_mean, divisor):
    """计算方差（可指定除数）"""
    sum_squared_deviations = sum((x - sample_mean)**2 for x in data)
    return sum_squared_deviations / divisor

# 总体参数（已知）
population_mean = 100
population_variance = 225  # σ² = 225
population_std = 15        # σ = 15

print("=" * 60)
print("样本方差无偏估计的蒙特卡洛模拟")
print("=" * 60)
print(f"\n总体参数（真实值）:")
print(f"  均值 μ = {population_mean}")
print(f"  方差 σ² = {population_variance}")
print(f"  标准差 σ = {population_std}")

# 模拟参数
sample_sizes = [5, 10, 30, 100]  # 不同的样本量
num_simulations = 10000           # 每个样本量重复10000次

print(f"\n模拟设置:")
print(f"  模拟次数: {num_simulations:,}")
print(f"  样本量: {sample_sizes}")

# 存储结果
results = {}

print("\n正在运行模拟...")
for n in sample_sizes:
    # 存储每次模拟的方差估计
    biased_estimates = []    # 除以N（有偏）
    unbiased_estimates = []  # 除以(N-1)（无偏）

    for sim in range(num_simulations):
        if sim % 2000 == 0 and sim > 0:
            print(f"  N={n}: 已完成 {sim}/{num_simulations} 次模拟")

        # 从正态总体中抽取样本
        sample = generate_normal_sample(population_mean, population_std, n)

        # 计算样本均值
        sample_mean = calculate_mean(sample)

        # 有偏估计：除以N
        biased_var = calculate_variance(sample, sample_mean, n)
        biased_estimates.append(biased_var)

        # 无偏估计：除以(N-1)
        unbiased_var = calculate_variance(sample, sample_mean, n - 1)
        unbiased_estimates.append(unbiased_var)

    results[n] = {
        'biased': biased_estimates,
        'unbiased': unbiased_estimates
    }

print("\n模拟完成！")

# 打印结果
print("\n" + "=" * 60)
print("模拟结果分析")
print("=" * 60)

for n in sample_sizes:
    biased_mean = calculate_mean(results[n]['biased'])
    unbiased_mean = calculate_mean(results[n]['unbiased'])

    biased_bias = biased_mean - population_variance
    unbiased_bias = unbiased_mean - population_variance

    biased_bias_pct = (biased_bias / population_variance) * 100
    unbiased_bias_pct = (unbiased_bias / population_variance) * 100

    print(f"\n样本量 N = {n}:")
    print(f"  真实方差 σ² = {population_variance}")
    print(f"  " + "-" * 50)
    print(f"  有偏估计 (除以N):")
    print(f"    平均值 = {biased_mean:.2f}")
    print(f"    偏差 = {biased_bias:.2f} ({biased_bias_pct:+.2f}%)")
    print(f"  " + "-" * 50)
    print(f"  无偏估计 (除以N-1):")
    print(f"    平均值 = {unbiased_mean:.2f}")
    print(f"    偏差 = {unbiased_bias:.2f} ({unbiased_bias_pct:+.2f}%)")
    print(f"  " + "-" * 50)

    # 理论偏差
    theoretical_bias = -population_variance / n
    theoretical_bias_pct = (theoretical_bias / population_variance) * 100
    print(f"  理论偏差 (有偏估计): {theoretical_bias:.2f} ({theoretical_bias_pct:.2f}%)")

# 数学证明
print("\n" + "=" * 60)
print("数学原理")
print("=" * 60)
print("""
为什么除以N是有偏的？

关键推导：
  E[Σ(Yᵢ - Ȳ)²] = E[Σ(Yᵢ - μ + μ - Ȳ)²]
                = E[Σ(Yᵢ - μ)²] - N·E[(Ȳ - μ)²]
                = N·σ² - N·(σ²/N)
                = N·σ² - σ²
                = (N-1)·σ²

因此：
  有偏估计：E[Σ(Yᵢ - Ȳ)² / N] = (N-1)·σ² / N = σ²·(N-1)/N ≠ σ²
  无偏估计：E[Σ(Yᵢ - Ȳ)² / (N-1)] = (N-1)·σ² / (N-1) = σ²

关键洞察：
  1. 用样本均值Ȳ代替总体均值μ，会系统性地低估方差
  2. 因为Ȳ是"最接近"样本的点，用它计算的偏差会偏小
  3. 除以(N-1)正好修正了这个偏差
  4. 这就是"自由度"的由来：N个观测值，用掉1个自由度估计均值
""")

# 总结表格
print("\n" + "=" * 60)
print("总结表格")
print("=" * 60)
print(f"{'样本量':^10} {'有偏估计':^15} {'无偏估计':^15} {'偏差改善':^15}")
print("-" * 60)
for n in sample_sizes:
    biased_mean = calculate_mean(results[n]['biased'])
    unbiased_mean = calculate_mean(results[n]['unbiased'])

    biased_error = abs(biased_mean - population_variance)
    unbiased_error = abs(unbiased_mean - population_variance)

    improvement = ((biased_error - unbiased_error) / biased_error) * 100

    print(f"{n:^10} {biased_mean:^15.2f} {unbiased_mean:^15.2f} {improvement:^15.1f}%")
