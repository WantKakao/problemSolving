import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append([*map(int, input().split())])

sumGraph = [[0 for _ in range(n+1)] for _ in range(n+1)]
sumGraph[0][0] = 0
for j in range(1, n+1):
    sumGraph[0][j] = 0
for i in range(1, n+1):
    sumGraph[i][0] = 0

for i in range(1, n+1):
    for j in range(1, n+1):
        sumGraph[i][j] = sumGraph[i-1][j] + sumGraph[i][j-1] - sumGraph[i-1][j-1] + graph[i-1][j-1]

for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    answer = sumGraph[x2][y2] - sumGraph[x1-1][y2] - sumGraph[x2][y1-1] + sumGraph[x1-1][y1-1]
    print(answer)