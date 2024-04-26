import sys
input = sys.stdin.readline

n, k = map(int, input().split())
coins = []
for _ in range(n):
    coins.append(int(input()))

coins.sort()
dp = [1] + [0 for _ in range(k)]
for i in range(coins[0], k+1, coins[0]):
    dp[i] = 1
for coin in coins[1:]:
    for i in range(coin, k+1):
        dp[i] = dp[i] + dp[i-coin]

print(dp[k])