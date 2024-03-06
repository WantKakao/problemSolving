from collections import deque

m, n = map(int, input().split())
tomato = []
for _ in range(n):
    tomato.append([*map(int, input().split())])

q = deque()
for i in range(n):
    for j in range(m):
        if tomato[i][j] == 1:
            q.append((i, j, 0))

while q:
    x, y, t = q.popleft()
    if 0 <= x-1 and tomato[x-1][y] == 0:
        q.append((x-1, y, t+1))
        tomato[x - 1][y] = 1
    if x + 1 < n and tomato[x + 1][y] == 0:
        q.append((x+1, y, t+1))
        tomato[x + 1][y] = 1
    if 0 <= y-1 and tomato[x][y-1] == 0:
        q.append((x, y-1, t+1))
        tomato[x][y - 1] = 1
    if y + 1 < m and tomato[x][y+1] == 0:
        q.append((x, y+1, t+1))
        tomato[x][y + 1] = 1

flag = 0
for i in range(n):
    for j in range(m):
        if tomato[i][j] == 0:
            flag = 1

if not flag:
    print(t)
else:
    print(-1)