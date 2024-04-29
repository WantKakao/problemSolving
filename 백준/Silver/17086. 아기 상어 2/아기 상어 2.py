import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))


def bfs(x, y):
    visited = [[False for _ in range(m)] for _ in range(n)]
    visited[x][y] = True
    q = deque([(x, y, 1)])
    dx = [-1, 1, 0, 0, -1, -1, 1, 1]
    dy = [0, 0, -1, 1, -1, 1, -1, 1]
    while q:
        x_cor, y_cor, dis = q.popleft()
        for t in range(8):
            nx = x_cor + dx[t]
            ny = y_cor + dy[t]
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                visited[nx][ny] = True
                if arr[nx][ny] == 1:
                    return dis
                else:
                    q.append((nx, ny, dis+1))


ans = 0
for i in range(n):
    for j in range(m):
        if arr[i][j] == 0:
            temp = bfs(i, j)
            ans = max(ans, temp)
print(ans)