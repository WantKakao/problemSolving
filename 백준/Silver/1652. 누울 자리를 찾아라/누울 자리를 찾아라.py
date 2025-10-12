n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(str, input())))
    
hor, ver = 0, 0
for i in range(n):
    for j in range(2, n):
        if graph[i][j] == 'X' and graph[i][j-1] == graph[i][j-2] == '.':
            hor += 1
    if n >= 2 and graph[i][n-1] == graph[i][n-2] == '.':
        hor += 1
for j in range(n):
    for i in range(2, n):
        if graph[i][j] == 'X' and graph[i-1][j] == graph[i-2][j] == '.':
            ver += 1
    if n >= 2 and graph[n-1][j] == graph[n-2][j] == '.':
        ver += 1
print(hor, ver)