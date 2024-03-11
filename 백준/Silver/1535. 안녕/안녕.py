n = int(input())
hp = [*map(int, input().split())]
happy = [*map(int, input().split())]
dp = [[0 for _ in range(100)] for _ in range(n)]
for j in range(100):
    if j-hp[0] >= 0:
        dp[0][j] = happy[0]
    else:
        dp[0][j] = 0

for i in range(1, n):
    for j in range(100):
        if j-hp[i] >= 0:
            dp[i][j] = max(dp[i][j-1], dp[i-1][j], dp[i-1][j-hp[i]]+happy[i])
        else:
            dp[i][j] = max(dp[i][j-1], dp[i-1][j])
print(dp[n-1][99])