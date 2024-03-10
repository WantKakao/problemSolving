import copy
import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append([*map(int, input().split())])
answer = 0


def bfs():
    copyGraph = copy.deepcopy(graph)
    q = deque()
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    for i in range(n):
        for j in range(m):
            if copyGraph[i][j] == 2:
                q.append((i, j))
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and copyGraph[nx][ny] == 0:
                copyGraph[nx][ny] = 2
                q.append((nx, ny))
    ans = 0
    for i in range(n):
        for j in range(m):
            if copyGraph[i][j] == 0:
                ans += 1
    return ans


def dfs(i, j, c):
    global answer
    graph[i][j] = 1
    if c == 3:
        a = bfs()
        if a > answer:
            answer = a
    else:
        for x in range(i, n):
            for y in range(m):
                if graph[x][y] == 0:
                    dfs(x, y, c+1)
    graph[i][j] = 0
    return


for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            dfs(i, j, 1)

print(answer)
