n, k = map(int, input().split())
items = [0]
for _ in range(n):
    items.append([*map(int, input().split())])      # items = [[0], [weight, value], ..., ]
graph = [[0 for _ in range(k+1)] for _ in range(n+1)]
for j in range(1, k+1):
    if j >= items[1][0]:
        graph[1][j] = items[1][1]
for i in range(2, n+1):
    for j in range(1, k+1):
        if j >= items[i][0]:
            graph[i][j] = max(graph[i-1][j], graph[i][j-1], graph[i-1][j-items[i][0]]+items[i][1])
        else:
            graph[i][j] = max(graph[i - 1][j], graph[i][j - 1])

print(graph[-1][-1])