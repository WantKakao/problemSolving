m, n = map(int, input().split())
graph = []
for _ in range(m):
    graph.append(list(map(str, input().rstrip())))
visited = [[False for _ in range(n)] for _ in range(m)]
ans = 0


def dfs(x, y, t):
    visited[x][y] = True
    if t == '|':
        new_x = x + 1
        if new_x < m and visited[new_x][y] == False and graph[x][y] == graph[new_x][y]:
            dfs(new_x, y, t)
    else:
        new_y = y + 1
        if new_y < n and visited[x][new_y] == False and graph[x][y] == graph[x][new_y]:
            dfs(x, new_y, t)
    return


for i in range(m):
    for j in range(n):
        if not visited[i][j]: # False 일시 실행
            ans += 1
            dfs(i, j, graph[i][j])

print(ans)