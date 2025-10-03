import sys
input = sys.stdin.readline

N, K = map(int, input().split())
heights = [int(input()) for _ in range(N)]

# dp[mask][last] = 경우의 수
dp = [[0] * N for _ in range(1 << N)]

# 초기값
for i in range(N):
    dp[1 << i][i] = 1

# DP 전개
for mask in range(1 << N):
    for last in range(N):
        if not (mask & (1 << last)):
            continue
        if dp[mask][last] == 0:
            continue
        for nxt in range(N):
            if mask & (1 << nxt):
                continue
            if abs(heights[last] - heights[nxt]) > K:
                dp[mask | (1 << nxt)][nxt] += dp[mask][last]

# 정답 계산
ans = sum(dp[(1 << N) - 1][i] for i in range(N))
print(ans)
