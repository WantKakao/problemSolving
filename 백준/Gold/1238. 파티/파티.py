import sys
from heapq import heappop, heappush

input = sys.stdin.readline

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    pq = [(0, start)]

    while pq:
        current_distance, current_node = heappop(pq)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heappush(pq, (distance, neighbor))

    return distances

n, m, x = map(int, input().split())
graph = {node: {} for node in range(1, n+1)}
reverse_graph = {node: {} for node in range(1, n+1)}

for _ in range(m):
    s, e, c = map(int, input().split())
    graph[s][e] = c
    reverse_graph[e][s] = c

x_to_all = dijkstra(graph, x)
all_to_x = dijkstra(reverse_graph, x)

longest = 0
for i in range(1, n+1):
    if x_to_all[i] + all_to_x[i] > longest:
        longest = x_to_all[i] + all_to_x[i]

print(longest)
