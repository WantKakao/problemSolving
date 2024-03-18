import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
cheese = []
for _ in range(n):
    cheese.append([*map(int, input().split())])
on_air = [[0 for _ in range(m)] for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
count = 0
for i in range(n):
    count += cheese[i].count(1)

q = deque()
q.append((0, 0))
on_air[0][0] = 1
while q:
    x, y = q.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and cheese[nx][ny] == 0 and on_air[nx][ny] == 0:
            on_air[nx][ny] = 1
            q.append((nx, ny))

t = 0
temp = 0
while count > 0:
    temp = count
    q2 = deque()
    for i in range(n):
        for j in range(m):
            if cheese[i][j] == 1 and on_air[i][j] == 0:
                for h in range(4):
                    ni = i + dx[h]
                    nj = j + dy[h]
                    if 0 <= ni < n and 0 <= nj < m and on_air[ni][nj] == 1:
                        count -= 1
                        q2.append((i, j))
                        break
    t += 1
    while q2:
        x, y = q2.popleft()
        on_air[x][y] = 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and cheese[nx][ny] == 0 and on_air[nx][ny] == 0:
                on_air[nx][ny] = 1
                q2.append((nx, ny))

print(t)
print(temp)
