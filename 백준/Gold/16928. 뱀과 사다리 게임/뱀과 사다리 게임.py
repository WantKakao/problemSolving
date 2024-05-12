import sys
input = sys.stdin.readline

n, m = map(int, input().split())
ladder, snake = [], []
for _ in range(n):
    start, end = map(int, input().split())
    ladder.append((start, end))
for _ in range(m):
    start, end = map(int, input().split())
    snake.append((start, end))

dp = [100 for _ in range(106)]
dp[1] = 0
for _ in range(2):
    for i in range(1, 100):
        for j in range(1, 7):
            temp = True
            for a, b in ladder:
                if a == i+j:
                    dp[b] = min(dp[b], dp[i]+1)
                    temp = False
            for a, b in snake:
                if a == i+j:
                    dp[b] = min(dp[b], dp[i]+1)
                    temp = False
            if temp:
                dp[i+j] = min(dp[i]+1, dp[i+j])

print(dp[100])
