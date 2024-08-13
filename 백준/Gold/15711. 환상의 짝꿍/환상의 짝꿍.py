import sys
import math
import random


# 에라토스테네스의 체로 소수 리스트 생성
def sieve(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False
    return [x for x in range(2, n + 1) if is_prime[x]]


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

    for _ in range(k):
        a = random.randint(2, n - 2)
        if not check(a, d, n, r):
            return False
    return True


# 최대 2 * 10^6까지 소수 리스트 생성
max_limit = int(2 * 10 ** 6)
small_primes = sieve(max_limit)

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