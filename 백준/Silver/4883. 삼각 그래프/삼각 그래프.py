import sys
input = sys.stdin.readline

t = 1
while True:
    n = int(input())

    if n == 0:
        break

    graph = []
    for _ in range(n):
        graph.append([*map(int, input().split())])

    dp = [[1e6, graph[0][1], graph[0][1]+graph[0][2]] for _ in range(n)]
    for i in range(1, n):
        dp[i][0] = min(dp[i-1][0], dp[i-1][1]) + graph[i][0]
        dp[i][1] = min(dp[i-1][0], dp[i-1][1], dp[i-1][2]) + graph[i][1]
        dp[i][1] = min(dp[i][1], dp[i][0] + graph[i][1])
        dp[i][2] = min(dp[i-1][1], dp[i-1][2]) + graph[i][2]
        dp[i][2] = min(dp[i][2], dp[i][1] + graph[i][2])

    print(f'{t}. {dp[n-1][1]}')
    t += 1
