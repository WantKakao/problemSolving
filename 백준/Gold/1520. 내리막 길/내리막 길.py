import heapq
import sys
input = sys.stdin.readline

m, n = map(int, input().split())
graph = []
for _ in range(m):
    graph.append([*map(int, input().split())])

count = [[0 for _ in range(n)] for _ in range(m)]
count[0][0] = 1
q = [(-graph[0][0], 0, 0)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

while q:
    height, x, y = heapq.heappop(q)
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < m and 0 <= ny < n and graph[nx][ny] < -height:
            if count[nx][ny] == 0:
                heapq.heappush(q, (-graph[nx][ny], nx, ny))
            count[nx][ny] += count[x][y]

print(count[m-1][n-1])