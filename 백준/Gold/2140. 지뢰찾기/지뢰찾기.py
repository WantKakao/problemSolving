import sys
input = sys.stdin.readline

n = int(input())
graph = []
for _ in range(n):
    graph.append([*map(str, input().rstrip())])

# print(graph)
if graph[0][0] == '1':
    graph[1][1] = '*'
if graph[0][n-1] == '1':
    graph[1][n-2] = '*'
if graph[n-1][0] == '1':
    graph[n-2][1] = '*'
if graph[n-1][n-1] == '1':
    graph[n-2][n-2] = '*'

def check(i, j, k, graph):
    cnt = 0
    if i == 0:
        if graph[i+1][j-1] == '*':
            cnt += 1
        if graph[i+1][j] == '*':
            cnt += 1
        if graph[i+1][j+1] == '*':
            cnt += 1
        if cnt == k:
            return
        else:
            graph[i+1][j+1] = '*'
            return
    elif i == n-1:
        if graph[i-1][j - 1] == '*':
            cnt += 1
        if graph[i-1][j] == '*':
            cnt += 1
        if graph[i-1][j + 1] == '*':
            cnt += 1
        if cnt == k:
            return
        else:
            graph[i-1][j + 1] = '*'
            return
    elif j == 0:
        if graph[i-1][j+1] == '*':
            cnt += 1
        if graph[i][j+1] == '*':
            cnt += 1
        if graph[i+1][j+1] == '*':
            cnt += 1
        if cnt == k:
            return
        else:
            graph[i+1][j+1] = '*'
            return
    elif j == n-1:
        if graph[i-1][j-1] == '*':
            cnt += 1
        if graph[i][j-1] == '*':
            cnt += 1
        if graph[i+1][j-1] == '*':
            cnt += 1
        if cnt == k:
            return
        else:
            graph[i+1][j-1] = '*'
            return


for j in range(1, n-1):
    k = int(graph[0][j])
    check(0, j, k, graph)
    k2 = int(graph[n-1][j])
    check(n-1, j, k2, graph)

for i in range(1, n-1):
    k = int(graph[i][0])
    check(i, 0, k, graph)
    k2 = int(graph[i][n-1])
    check(i, n-1, k2, graph)

count = 0
for i in range(n):
    count += graph[i].count('*')

if n >= 5:
    print(count + (n-4) * (n-4))
else:
    print(count)