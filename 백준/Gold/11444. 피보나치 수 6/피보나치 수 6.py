MOD = 10**9 + 7

def mat_mult(a, b):
    return [
        [(a[0][0]*b[0][0] + a[0][1]*b[1][0]) % MOD,
         (a[0][0]*b[0][1] + a[0][1]*b[1][1]) % MOD],
        [(a[1][0]*b[0][0] + a[1][1]*b[1][0]) % MOD,
         (a[1][0]*b[0][1] + a[1][1]*b[1][1]) % MOD]
    ]

def mat_pow(mat, power):
    result = [[1, 0], [0, 1]]  # 단위행렬
    while power > 0:
        if power % 2 == 1:
            result = mat_mult(result, mat)
        mat = mat_mult(mat, mat)
        power //= 2
    return result

def fib(n):
    if n == 0:
        return 0
    base = [[1, 1], [1, 0]]
    res = mat_pow(base, n - 1)
    return res[0][0]

n = int(input())
print(fib(n))
