import sys
input = sys.stdin.readline
from collections import deque

m, n, h = map(int, input().split())
tomato = [[] for _ in range(h)]
for k in range(h):
    for j in range(n):
        tomato[k].append([*map(int, input().split())])
# tomato[h][n][m] 가 되버림
INF = 10e9
cook = [[[INF for _ in range(m)] for _ in range(n)] for _ in range(h)]
for k in range(h):
    for j in range(n):
        for i in range(m):
            if tomato[k][j][i] == 1:
                cook[k][j][i] = 0

d = [(-1,0,0),(1,0,0),(0,-1,0),(0,1,0),(0,0,-1),(0,0,1)]
q = deque()

def bfs():
    while q:
        x, y, z, c = q.popleft()
        for i in range(6):
            new_x = x + d[i][0]
            new_y = y + d[i][1]
            new_z = z + d[i][2]
            if new_x >= 0 and new_y >= 0 and new_z >= 0 and new_x < m and new_y < n and new_z < h:  # 범위 내
                if tomato[new_z][new_y][new_x] == 0 and cook[new_z][new_y][new_x] > c+1:
                    cook[new_z][new_y][new_x] = c+1
                    q.append((new_x, new_y, new_z, c+1))

for k in range(h):
    for j in range(n):
        for i in range(m):
            if tomato[k][j][i] == 1:
                q.append((i, j, k, 0))
bfs()

maximum = 0
for k in range(h):
    for j in range(n):
        for i in range(m):
            if cook[k][j][i] > maximum and tomato[k][j][i] != -1:
                maximum = cook[k][j][i]

if maximum == INF:
    print(-1)
else:
    print(maximum)