import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
arr = []
for _ in range(n):
    arr.append([*map(int, input().split())])

for i in range(n):
    for j in range(m):
        if arr[i][j] == 1:
            arr[i][j] = 1e6
        elif arr[i][j] == 2:
            arr[i][j] = 0
            q = deque([(i, j, 0)])

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
while q:
    x, y, c = q.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and c+1 < arr[nx][ny]:
            arr[nx][ny] = c+1
            q.append((nx, ny, c+1))

for i in range(n):
    for j in range(m):
        if arr[i][j] == 1e6:
            print(-1, end=' ')
        else:
            print(arr[i][j], end=' ')
    print()