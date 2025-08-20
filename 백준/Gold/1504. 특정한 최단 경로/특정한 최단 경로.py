import heapq
import sys
input = sys.stdin.readline

def dijkstra(start):
    INF = 1e9
    distance = [INF] * (n+1)
    distance[start] = 0
    q = [(0, start)]
    
    while q:
        dist, now = heapq.heappop(q)
        if dist > distance[now]:
            continue
        for nxt, w in graph[now]:
            cost = dist + w
            if cost < distance[nxt]:
                distance[nxt] = cost
                heapq.heappush(q, (cost, nxt))
    return distance


n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))   # 방향 그래프 (양방향이면 v->u도 추가)
    graph[v].append((u, w))

a, b = map(int, input().split())
distances1 = dijkstra(1)
distances2 = dijkstra(a)
distances3 = dijkstra(b)

A = distances1[a] + distances2[b] + distances3[n]
B = distances1[b] + distances3[a] + distances2[n]
if A >= 1e9 and B >= 1e9:
    print(-1)
else:
    print(min(A, B))