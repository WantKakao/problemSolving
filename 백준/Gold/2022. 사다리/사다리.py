import math

def solve(x, y, c):
    left = 0
    right = min(x, y)

    for _ in range(100):  # 충분히 반복 (정밀도 확보)
        mid = (left + right) / 2

        h1 = math.sqrt(x*x - mid*mid)
        h2 = math.sqrt(y*y - mid*mid)

        val = (1/h1) + (1/h2)

        if val > 1/c:
            right = mid
        else:
            left = mid

    return left


# 입력 예시
x, y, c = map(float, input().split())
print(f"{solve(x, y, c):.6f}")
