"""
演示R²与调整R²的差异
展示为什么调整R²能有效惩罚无关变量
"""
import random
import math

random.seed(42)

def generate_normal(mu, sigma):
    """生成正态分布随机数"""
    u1 = random.random()
    u2 = random.random()
    z = math.sqrt(-2 * math.log(u1)) * math.cos(2 * math.pi * u2)
    return mu + sigma * z

def matrix_multiply(A, B):
    """矩阵乘法"""
    rows_A, cols_A = len(A), len(A[0])
    rows_B, cols_B = len(B), len(B[0])

    if cols_A != rows_B:
        raise ValueError("矩阵维度不匹配")

    result = [[0 for _ in range(cols_B)] for _ in range(rows_A)]
    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):
                result[i][j] += A[i][k] * B[k][j]
    return result

def transpose(matrix):
    """矩阵转置"""
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

def matrix_inverse_2x2(matrix):
    """2x2矩阵求逆"""
    a, b = matrix[0][0], matrix[0][1]
    c, d = matrix[1][0], matrix[1][1]

    det = a * d - b * c
    if abs(det) < 1e-10:
        raise ValueError("矩阵不可逆")

    return [[d/det, -b/det], [-c/det, a/det]]

def simple_ols(Y, X):
    """简单OLS回归（仅支持一个解释变量）"""
    n = len(Y)

    # 添加截距项
    X_with_const = [[1, x[0]] for x in X]

    # 计算 X'X
    X_t = transpose(X_with_const)
    XtX = matrix_multiply(X_t, X_with_const)

    # 计算 X'Y
    Y_matrix = [[y] for y in Y]
    XtY = matrix_multiply(X_t, Y_matrix)

    # 计算 (X'X)^(-1)
    XtX_inv = matrix_inverse_2x2(XtX)

    # 计算 β = (X'X)^(-1)X'Y
    beta = matrix_multiply(XtX_inv, XtY)

    # 预测值
    Y_pred = [beta[0][0] + beta[1][0] * x[0] for x in X]

    # 计算SSR和SST
    Y_mean = sum(Y) / n
    SSR = sum((Y[i] - Y_pred[i])**2 for i in range(n))
    SST = sum((Y[i] - Y_mean)**2 for i in range(n))

    # R²
    R2 = 1 - SSR / SST

    # 调整R² (K=1个解释变量)
    K = 1
    adj_R2 = 1 - (SSR / (n - K - 1)) / (SST / (n - 1))

    return {
        'beta': [beta[0][0], beta[1][0]],
        'Y_pred': Y_pred,
        'SSR': SSR,
        'SST': SST,
        'R2': R2,
        'adj_R2': adj_R2,
        'n': n,
        'K': K
    }

# 生成数据
print("=" * 70)
print("R² vs 调整R² 演示")
print("=" * 70)

# 真实的数据生成过程：Y = 10 + 5*X + ε
n = 50
print(f"\n数据生成过程（DGP）：")
print(f"  Y = 10 + 5·X + ε")
print(f"  其中 ε ~ N(0, 25)")
print(f"  样本量 N = {n}")

# 生成X1（真正有效的变量）
X1 = [generate_normal(5, 2) for _ in range(n)]

# 生成Y
Y = [10 + 5*x1 + generate_normal(0, 5) for x1 in X1]

# 生成X2（完全无关的噪声变量）
X2 = [generate_normal(0, 1) for _ in range(n)]

print("\n" + "=" * 70)
print("模型1：只用有效变量 X1")
print("=" * 70)

# 模型1：Y = β0 + β1*X1
model1 = simple_ols(Y, [[x1] for x1 in X1])

print(f"\n回归结果：")
print(f"  Ŷ = {model1['beta'][0]:.3f} + {model1['beta'][1]:.3f}·X1")
print(f"\n拟合优度：")
print(f"  R²          = {model1['R2']:.4f}")
print(f"  调整R²      = {model1['adj_R2']:.4f}")
print(f"  差异        = {model1['R2'] - model1['adj_R2']:.4f}")
print(f"\n自由度：")
print(f"  N = {model1['n']}")
print(f"  K = {model1['K']} (解释变量个数)")
print(f"  残差自由度 = N - K - 1 = {model1['n'] - model1['K'] - 1}")

# 手动计算调整R²以展示公式
print(f"\n调整R²的计算：")
print(f"  σ̂ε² = SSR/(N-K-1) = {model1['SSR']:.2f}/{model1['n']-model1['K']-1} = {model1['SSR']/(model1['n']-model1['K']-1):.4f}")
print(f"  σ̂y² = SST/(N-1)   = {model1['SST']:.2f}/{model1['n']-1} = {model1['SST']/(model1['n']-1):.4f}")
print(f"  R̄² = 1 - σ̂ε²/σ̂y² = 1 - {model1['SSR']/(model1['n']-model1['K']-1):.4f}/{model1['SST']/(model1['n']-1):.4f} = {model1['adj_R2']:.4f}")

print("\n" + "=" * 70)
print("模型2：加入无关变量 X2（纯噪声）")
print("=" * 70)

# 模型2：Y = β0 + β1*X2（用噪声变量）
model2 = simple_ols(Y, [[x2] for x2 in X2])

print(f"\n回归结果：")
print(f"  Ŷ = {model2['beta'][0]:.3f} + {model2['beta'][1]:.3f}·X2")
print(f"\n拟合优度：")
print(f"  R²          = {model2['R2']:.4f}")
print(f"  调整R²      = {model2['adj_R2']:.4f}")

print("\n" + "=" * 70)
print("对比分析")
print("=" * 70)

print(f"\n{'模型':<20} {'变量':<10} {'R²':<10} {'调整R²':<10} {'差异':>10}")
print("-" * 70)
print(f"{'模型1（有效变量）':<20} {'X1':<10} {model1['R2']:<10.4f} {model1['adj_R2']:<10.4f} {model1['R2']-model1['adj_R2']:>10.4f}")
print(f"{'模型2（噪声变量）':<20} {'X2':<10} {model2['R2']:<10.4f} {model2['adj_R2']:<10.4f} {model2['R2']-model2['adj_R2']:>10.4f}")

print("\n" + "=" * 70)
print("关键观察")
print("=" * 70)
print(f"""
1. 有效变量（X1）：
   - R² = {model1['R2']:.4f}（高，因为X1确实解释了Y）
   - 调整R² = {model1['adj_R2']:.4f}（略低于R²，但仍然高）
   - 两者差异小，说明变量是值得的

2. 噪声变量（X2）：
   - R² = {model2['R2']:.4f}（可能不是0，因为随机相关）
   - 调整R² = {model2['adj_R2']:.4f}（可能为负！）
   - 调整R²显著低于R²，警告这个变量无效

3. 为什么调整R²可能为负？
   - 当模型比"只用均值"还差时，调整R²会是负数
   - 这是一个强烈的信号：模型无效！
   - 普通R²永远 ≥ 0，无法提供这个警告

4. 调整R²的惩罚机制：
   - 使用自由度 (N-K-1) 而不是样本量 N
   - K 越大，惩罚越重
   - 只有变量"足够好"，才能抵消惩罚并提高调整R²
""")

print("=" * 70)
print("数学公式验证")
print("=" * 70)

# 验证调整R²的等价公式
for i, model in enumerate([model1, model2], 1):
    alt_adj_r2 = 1 - (1 - model['R2']) * (model['n'] - 1) / (model['n'] - model['K'] - 1)
    print(f"\n模型{i}：")
    print(f"  方法1（直接计算）：R̄² = {model['adj_R2']:.6f}")
    print(f"  方法2（等价公式）：R̄² = 1 - (1-R²)·(N-1)/(N-K-1)")
    print(f"                         = 1 - (1-{model['R2']:.4f})·({model['n']}-1)/({model['n']}-{model['K']}-1)")
    print(f"                         = {alt_adj_r2:.6f}")
    print(f"  验证：两种方法相同 ✓" if abs(model['adj_R2'] - alt_adj_r2) < 1e-6 else "  错误！")

print("\n" + "=" * 70)
print("总结")
print("=" * 70)
print("""
调整R²通过引入自由度的概念，实现了对模型复杂度的自动惩罚。

关键机制：
  σ̂ε² = SSR / (N-K-1)  ← 自由度随K增加而减少

当你添加一个变量：
  - 如果它"足够好"：SSR下降幅度 > 自由度减少的影响 → R̄²上升
  - 如果它是噪声：SSR略微下降 < 自由度减少的影响 → R̄²下降

这不是人为的修正，而是正确使用无偏方差估计的自然结果！
""")
