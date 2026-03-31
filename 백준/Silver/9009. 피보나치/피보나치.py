import sys
input = sys.stdin.readline

# 피보나치 생성
fib = [1, 2]
while fib[-1] < 1_000_000_000:
    fib.append(fib[-1] + fib[-2])

T = int(input())
for _ in range(T):
    n = int(input())
    ans = []

    for i in range(len(fib)-1, -1, -1):
        if fib[i] <= n:
            n -= fib[i]
            ans.append(fib[i])
        if n == 0:
            break

    ans.sort()
    print(*ans)
