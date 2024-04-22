import heapq
import sys
input = sys.stdin.readline


def dijkstra(graph, start):
    distance = {node: float('inf') for node in graph.keys()}
    distance[start] = 0
    q = [(0, start)]

    while q:
        dist, node = heapq.heappop(q)

        if dist > distance[node]:
            continue

        for neighbor, cost in graph[node].items():
            d = dist + cost
            if d < distance[neighbor]:
                distance[neighbor] = d
                heapq.heappush(q, (d, neighbor))

    return distance


n, m = map(int, input().split())
arr = {node: {} for node in range(1, n+1)}
for _ in range(m):
    a, b, c = map(int, input().split())

    if b in arr[a].keys():
        arr[a][b] = min(arr[a][b], c)
    else:
        arr[a][b] = c

    if a in arr[b].keys():
        arr[b][a] = min(arr[a][b], c)
    else:
        arr[b][a] = c

shortest = dijkstra(arr, 1)
print(shortest[n])