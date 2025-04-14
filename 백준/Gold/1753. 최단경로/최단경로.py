import heapq

V, e = map(int, input().split())
start_v = int(input())
graph = [{} for _ in range(V+1)]
for _ in range(e):
    u, v, w = map(int, input().split())
    if v not in graph[u] or graph[u][v] > w:
        graph[u][v] = w

def dijkstra(start, graph, n):
    distance = [float('inf')] * (n+1)
    distance[start] = 0
    queue = [(0, start)]

    while queue:
        dist, now = heapq.heappop(queue)

        if dist > distance[now]:
            continue

        for next, weight in graph[now].items():
            cost = dist + weight
            if cost < distance[next]:
                distance[next] = cost
                heapq.heappush(queue, (cost, next))

    return distance

distances = dijkstra(start_v, graph, V)
for i in range(1, V+1):
    if distances[i] == float('inf'):
        print('INF')
    else:
        print(distances[i])