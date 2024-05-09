import sys
input = sys.stdin.readline

N = int(input())
consulting = []
for _ in range(N):
    t, p = map(int, input().split())
    consulting.append((t, p))

dp = [0 for _ in range(N+1)]
for i in range(N):
    T, P = consulting[i]
    if i > 0:
        dp[i] = max(dp[i-1], dp[i])
    if i+T <= N:
        dp[i+T] = max(dp[i]+P, dp[i+T])

dp[N] = max(dp[N], dp[N-1])
print(dp[N])