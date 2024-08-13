import sys
import random


# 밀러-라빈 소수 판별법
def miller_rabin(n, k=5):  # k는 테스트 횟수
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False

    # n을 d*2^r + 1 형태로 분해
    r, d = 0, n - 1
    while d % 2 == 0:
        r += 1
        d //= 2

    def check(a, d, n, r):
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            return True
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                return True
        return False

    a = 2
    if not check(a, d, n, r):
        return False
    return True


# 입력 받기
T = int(input().strip())

results = []
for _ in range(T):
    A, B = map(int, input().split())
    S = A + B

    if S < 4:
        results.append("NO")
    elif S % 2 == 0:
        results.append("YES")
    else:
        if miller_rabin(S - 2):
            results.append("YES")
        else:
            results.append("NO")

# 결과 출력
sys.stdout.write("\n".join(results) + "\n")