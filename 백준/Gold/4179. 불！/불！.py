from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append([*map(str, input().rstrip())])

q = deque()
for i in range(n):
    for j in range(m):
        if graph[i][j] == 'F':
            q.append((1, i, j, 0))
for i in range(n):
    for j in range(m):
        if graph[i][j] == 'J':
            q.append((0, i, j, 0))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
found = False
while q:
    jf, x, y, t = q.popleft()
    if x == 0 or x == n-1 or y == 0 or y == m-1:
        if jf == 0:
            found = True
            print(t+1)
            break

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == '.':
            graph[nx][ny] = 'J' if jf == 0 else 'F'
            q.append((jf, nx, ny, t+1))

if not found:
    print("IMPOSSIBLE")