from collections import deque

def bfs(start, graph, visited):
    queue = deque([start])
    visited[start] = True
    count = 1
    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                count += 1
                queue.append(neighbor)
    return count

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[b].append(a)  # 간선 뒤집어서 저장

max_hack = 0
result = []

for i in range(1, n + 1):
    visited = [False] * (n + 1)
    cnt = bfs(i, graph, visited)
    if cnt > max_hack:
        max_hack = cnt
        result = [i]
    elif cnt == max_hack:
        result.append(i)

print(' '.join(map(str, result)))
