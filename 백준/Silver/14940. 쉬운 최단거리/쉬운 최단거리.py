import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append([*map(int, input().split())])

q = deque()
distance = [[-1 for _ in range(m)] for _ in range(n)]
for i in range(n):
    for j in range(m):
        if graph[i][j] == 2:
            q.append((i, j, 0))
            distance[i][j] = 0
        elif graph[i][j] == 0:
            distance[i][j] = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
while q:
    i, j, k = q.popleft()
    for dt in range(4):
        if 0<=i+dx[dt]<n and 0<=j+dy[dt]<m and distance[i+dx[dt]][j+dy[dt]] == -1:
            distance[i+dx[dt]][j+dy[dt]] = k+1
            q.append((i+dx[dt], j+dy[dt], k+1))

for i in range(n):
    for j in range(m):
        print(distance[i][j], end=' ')
    print()