import sys

input = sys.stdin.readline

t, w = map(int, input().split())

plum = []
for _ in range(t):
    plum.append(int(input()))

dp = [[0 for _ in range(t)] for _ in range(w+1)]

for i in range(w+1):
    if i % 2 == 0:
        if plum[0] == 1:
            dp[i][0] = 1
        else:
            dp[i][0] = 0
    else:
        if plum[0] == 1:
            dp[i][0] = 0
        else:
            dp[i][0] = 1

for j in range(1, t):
    if plum[j] == 1:
        dp[0][j] = dp[0][j-1] + 1
    else:
        dp[0][j] = dp[0][j-1]

for i in range(1, w+1):
    for j in range(1, t):
        if i % 2 == 0:
            if plum[j] == 1:
                dp[i][j] = max(dp[i][j-1], dp[i-1][j-1]) + 1
            else:
                dp[i][j] = max(dp[i][j-1], dp[i-1][j-1])
        else:
            if plum[j] == 1:
                dp[i][j] = max(dp[i][j-1], dp[i-1][j-1])
            else:
                dp[i][j] = max(dp[i][j-1], dp[i-1][j-1]) + 1

ans = 0
for d in dp:
    if d[-1] > ans:
        ans = d[-1]
print(ans)
