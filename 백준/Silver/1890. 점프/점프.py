n = int(input())
graph = [[*map(int, input().split())] for _ in range(n)]
# print(graph)
dp = [[0 for _ in range(n)] for _ in range(n)]
dp[0][0] = 1
# 이중 for loop 로 돌리면 값이 무조건 보장

for x in range(n):
    for y in range(n):
        j = graph[x][y]
        if j == 0:
            continue
        if x + j < n:
            dp[x+j][y] += dp[x][y]
        if y + j < n:
            dp[x][y+j] += dp[x][y]

print(dp[-1][-1])
