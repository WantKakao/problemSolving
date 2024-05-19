import sys
input = sys.stdin.readline

test = int(input())
for _ in range(test):
    n = int(input())
    sticker = []
    for _ in range(2):
        sticker.append([0] + list(map(int, input().split())))

    dp = [[0 for _ in range(n+1)] for _ in range(2)]
    dp[0][1] = sticker[0][1]
    dp[1][1] = sticker[1][1]
    for j in range(2, n+1):
        dp[0][j] = max(dp[1][j - 1], dp[1][j - 2]) + sticker[0][j]
        dp[1][j] = max(dp[0][j - 1], dp[0][j - 2]) + sticker[1][j]

    print(max(dp[0][n], dp[1][n]))