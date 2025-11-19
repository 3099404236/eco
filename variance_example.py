"""
直观示例：用一个具体的小样本演示方差估计的差异
"""

# 假设我们有一个小样本（只有5个观测值）
sample = [95, 102, 88, 110, 105]

print("=" * 60)
print("直观示例：方差估计的差异")
print("=" * 60)

print(f"\n样本数据：{sample}")
print(f"样本量 N = {len(sample)}")

# 计算样本均值
sample_mean = sum(sample) / len(sample)
print(f"样本均值 Ȳ = {sample_mean:.2f}")

# 计算离差
print("\n每个观测值的离差 (Yᵢ - Ȳ):")
deviations = []
for i, y in enumerate(sample):
    deviation = y - sample_mean
    deviations.append(deviation)
    print(f"  Y{i+1} = {y:3}, 离差 = {deviation:+6.2f}")

# 计算离差平方和
squared_deviations = [d**2 for d in deviations]
sum_squared_deviations = sum(squared_deviations)

print(f"\n离差平方 (Yᵢ - Ȳ)²:")
for i, sq_dev in enumerate(squared_deviations):
    print(f"  ({deviations[i]:+6.2f})² = {sq_dev:6.2f}")

print(f"\n离差平方和 Σ(Yᵢ - Ȳ)² = {sum_squared_deviations:.2f}")

# 两种估计
n = len(sample)
biased_var = sum_squared_deviations / n
unbiased_var = sum_squared_deviations / (n - 1)

print("\n" + "=" * 60)
print("两种方差估计")
print("=" * 60)

print(f"\n方法1：有偏估计（除以N）")
print(f"  s² = Σ(Yᵢ - Ȳ)² / N")
print(f"     = {sum_squared_deviations:.2f} / {n}")
print(f"     = {biased_var:.2f}")

print(f"\n方法2：无偏估计（除以N-1）")
print(f"  s² = Σ(Yᵢ - Ȳ)² / (N-1)")
print(f"     = {sum_squared_deviations:.2f} / {n-1}")
print(f"     = {unbiased_var:.2f}")

print(f"\n差异：{unbiased_var - biased_var:.2f}")
print(f"无偏估计比有偏估计大 {((unbiased_var / biased_var - 1) * 100):.1f}%")

print("\n" + "=" * 60)
print("为什么要用无偏估计？")
print("=" * 60)
print("""
想象你重复这个实验10000次（每次抽5个数）：

- 如果用"除以N"，平均下来会系统性地低估真实方差约20%
- 如果用"除以N-1"，平均下来会非常接近真实方差

这就是为什么统计学中标准的样本方差公式要除以(N-1)！
""")

print("=" * 60)
print("自由度的直观理解")
print("=" * 60)
print("""
自由度 = N - 1 的含义：

你有N个观测值，但当你计算离差 (Yᵢ - Ȳ) 时：
  - 你已经用这N个观测值计算了样本均值Ȳ
  - 这就"用掉"了1个自由度
  - 实际上只剩下(N-1)个"独立"的信息

数学上：如果你知道了(N-1)个离差和样本均值，
        最后一个离差就被确定了（因为Σ(Yᵢ - Ȳ) = 0）

例如在我们的例子中：
""")

print(f"  前4个离差：{', '.join(f'{d:+.2f}' for d in deviations[:-1])}")
print(f"  第5个离差必须是：{deviations[-1]:+.2f}")
print(f"  (因为它们的和必须等于0)")
print(f"  验证：{' + '.join(f'({d:+.2f})' for d in deviations)} = {sum(deviations):.10f}")
