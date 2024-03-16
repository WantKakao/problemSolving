import sys
input = sys.stdin.readline

city = int(input())
bus = int(input())
graph = [[1e9 for _ in range(city)] for _ in range(city)]
for _ in range(bus):
    start, end, cost = map(int, input().split())
    if graph[start-1][end-1] > cost:
        graph[start-1][end-1] = cost

for i in range(city):
    graph[i][i] = 0

for k in range(city):
    for i in range(city):
        for j in range(city):
            graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])

for i in range(city):
    for j in range(city):
        if graph[i][j] == 1e9:
            graph[i][j] = 0

for i in range(city):
    for j in range(city):
        print(graph[i][j], end=' ')
    print()