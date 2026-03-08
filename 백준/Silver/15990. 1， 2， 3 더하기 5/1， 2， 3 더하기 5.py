import sys
input = sys.stdin.readline

MOD = 1000000009

t = int(input())
nums = [int(input()) for _ in range(t)]
m = max(nums)

dp = [[0]*(m+1) for _ in range(4)]

dp[1][1], dp[1][2], dp[1][3] = 1, 0, 1
dp[2][1], dp[2][2], dp[2][3] = 0, 1, 1
dp[3][1], dp[3][2], dp[3][3] = 0, 0, 1

for i in range(4, m+1):
    if i-1 > 0:
        dp[1][i] = (dp[2][i-1] + dp[3][i-1]) % MOD
    if i-2 > 0:
        dp[2][i] = (dp[1][i-2] + dp[3][i-2]) % MOD
    if i-3 > 0:
        dp[3][i] = (dp[1][i-3] + dp[2][i-3]) % MOD

for n in nums:
    print((dp[1][n] + dp[2][n] + dp[3][n]) % MOD)
