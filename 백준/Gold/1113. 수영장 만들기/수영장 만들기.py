import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
pool = [list(map(int, input().rstrip())) for _ in range(n)]

def bfs(i, j, k):
    visited[i][j] = True
    q = deque()
    q.append((i, j))
    temp = 1
    flag = False
    while q:
        x, y = q.popleft()
        for dx, dy in [(0,1),(0,-1),(1,0),(-1,0)]:
            if 0 <= x+dx < n and 0 <= y+dy < m:
                if not visited[x+dx][y+dy] and pool[x+dx][y+dy] <= k:
                    visited[x+dx][y+dy] = True
                    q.append((x+dx, y+dy))
                    temp += 1
                    if x+dx==0 or x+dx==n-1 or y+dy==0 or y+dy==m-1:
                        flag = True
    if not flag:
        return temp
    return 0

ans = 0
for k in range(1, 9):
    visited = [[False for _ in range(m)] for _ in range(n)]
    for i in range(1, n-1):
        for j in range(1, m-1):
            if pool[i][j] <= k and not visited[i][j]:
                value = bfs(i, j, k)
                ans += value
print(ans)