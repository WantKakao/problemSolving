n, m = map(int, input().split())
graph = []
for _ in range(m):
    graph.append(input())
    
visited = [[False for _ in range(n)] for _ in range(m)]
d = [(0, 1), (0, -1), (1, 0), (-1, 0)]
q = []
white, blue = 0, 0
for i in range(m):
    for j in range(n):
        if not visited[i][j]:
            visited[i][j] = True
            q.append((i, j, graph[i][j]))
            temp = 1
            while q:
                x, y, color = q.pop()
                for k in range(4):
                    if 0 <= x+d[k][0] < m and 0 <= y+d[k][1] < n and not visited[x+d[k][0]][y+d[k][1]]:
                        if graph[x+d[k][0]][y+d[k][1]] == color:
                            visited[x+d[k][0]][y+d[k][1]] = True
                            q.append((x+d[k][0], y+d[k][1], graph[x+d[k][0]][y+d[k][1]]))
                            temp += 1
            if graph[i][j] == 'W':
                white += temp * temp
            else:
                blue += temp * temp

print(white, blue)