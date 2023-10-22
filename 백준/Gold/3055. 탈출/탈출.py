import sys
input = sys.stdin.readline
from collections import deque

m, n = map(int, input().split())
graph = []
for _ in range(m):
    graph.append([*map(str, input().rstrip())])
# print(graph)
q = deque()
d = [(-1, 0), (0, -1), (1, 0), (0, 1)]


def bfs():
    while q:
        x, y, t, c = q.popleft()    # x 좌표, y 좌표, time, 고슴도치 or 물
        for i in range(4):
            new_x = x + d[i][0]
            new_y = y + d[i][1]
            if new_x >= 0 and new_y >= 0 and new_x < m and new_y < n:   # 범위 안
                if c == 1 and graph[new_x][new_y] == '.':   # 물
                    q.append((new_x, new_y, t+1, 1))
                    graph[new_x][new_y] = '*'
                elif c == 0 and graph[new_x][new_y] == '.': # 고슴도치
                    q.append((new_x, new_y, t+1, 0))
                    graph[new_x][new_y] = 'S'
                elif c == 0 and graph[new_x][new_y] == 'D': # 도착시
                    return t+1
    return 'KAKTUS'

for i in range(m):
    for j in range(n):
        if graph[i][j] == '*':
            q.append((i, j, 0, 1))
for i in range(m):  # 물을 먼저 넣어줘야 함
    for j in range(n):
        if graph[i][j] == 'S':
            q.append((i, j, 0, 0))
print(bfs())