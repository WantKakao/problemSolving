from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
friendship = [[0 for _ in range(n+1)] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    friendship[a][b] = 1
    friendship[b][a] = 1

for i in range(1, n+1):
    q = deque()
    for j in range(1, n+1):
        if friendship[i][j] == 1:
            q.append((j, 1))
    while q:
        friend, bacon = q.popleft()
        for k in range(1, n+1):
            if friendship[i][k] == 0 and friendship[friend][k] == 1:
                q.append((k, bacon+1))
                friendship[i][k] = bacon+1

ans = 1e9
idx = 1
for i in range(1, n+1):
    temp = sum(friendship[i]) - friendship[i][i]
    if temp < ans:
        ans = temp
        idx = i

print(idx)