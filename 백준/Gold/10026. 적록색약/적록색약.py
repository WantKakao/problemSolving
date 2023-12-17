import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

n = int(input())
graph = []
for _ in range(n):
    graph.append([*map(str, input().rstrip())])
visit = [[0 for _ in range(n)] for _ in range(n)]
RG_visit = [[0 for _ in range(n)] for _ in range(n)]
count = 0
RG_count = 0
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def bfs(x, y, visit, color):
    visit[x][y] = 1
    for i in range(4):
        next_x = x+dx[i]
        next_y = y+dy[i]
        if next_x >= 0 and next_x < n and next_y >=0 and next_y < n:
            if graph[next_x][next_y] == color and not visit[next_x][next_y]:
                bfs(next_x, next_y, visit, color)


for i in range(n):
    for j in range(n):
        if visit[i][j] == 0:
            count += 1
            bfs(i, j, visit, graph[i][j])

print(count, end=' ')

for i in range(n):
    for j in range(n):
        if graph[i][j] == 'G':
            graph[i][j] = 'R'

for i in range(n):
    for j in range(n):
        if RG_visit[i][j] == 0:
            RG_count += 1
            bfs(i, j, RG_visit, graph[i][j])

print(RG_count)