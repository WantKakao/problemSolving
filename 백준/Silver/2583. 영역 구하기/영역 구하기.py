import sys
from collections import deque
input = sys.stdin.readline
n, m, k = map(int, input().split())
graph = [[0 for _ in range(m)] for _ in range(n)]
for _ in range(k):
    y1, x1, y2, x2 = map(int, input().split())
    for i in range(x1, x2):
        for j in range(y1, y2):
            graph[i][j] = 1

ans = 0
arr = []
q = deque()
d = [(-1, 0), (1, 0), (0, -1), (0, 1)]
visited = [[0 for _ in range(m)] for _ in range(n)]
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            ans += 1
            temp = 1
            visited[i][j] = 1
            graph[i][j] = 1
            q.append((i, j))
            while q:
                i, j = q.popleft()
                for k in range(4):
                    ni = i + d[k][0]
                    nj = j + d[k][1]
                    if 0 <= ni < n and 0 <= nj < m and graph[ni][nj] == 0 and visited[ni][nj] == 0:
                        visited[ni][nj] = 1
                        q.append((ni, nj))
                        graph[ni][nj] = 1
                        temp += 1
            arr.append(temp)
arr.sort()
print(ans)
for a in arr:
    print(a, end=' ')
