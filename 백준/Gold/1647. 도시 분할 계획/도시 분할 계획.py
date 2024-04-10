def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]


def union(parent, rank, a, b):
    rootA = find(parent, a)
    rootB = find(parent, b)

    if rank[rootA] < rank[rootB]:
        parent[rootA] = rootB
    else:
        parent[rootB] = rootA
        if rank[rootA] == rank[rootB]:
            rank[rootA] += 1


def kruskal(n, edges):
    # 정점 수 n, 간선 리스트 edges
    parent = [i for i in range(n)]
    rank = [0] * n
    mst_cost = 0
    mst_edges = []

    edges.sort(key=lambda x: x[2])  # 간선을 비용에 따라 정렬

    for a, b, cost in edges:
        if find(parent, a) != find(parent, b):
            union(parent, rank, a, b)
            mst_cost += cost
            mst_edges.append((a, b, cost))

    # mst_edges는 최소 스패닝 트리를 구성하는 간선들이며, 각 간선은 (a, b, cost) 형태
    return mst_cost, mst_edges


def solution(n, m, roads):
    # roads는 (A, B, C) 형태의 튜플 리스트, 여기서 A와 B는 집 번호, C는 유지비용
    mst_cost, mst_edges = kruskal(n + 1, roads)
    # 가장 비용이 큰 간선 제거를 위해
    max_edge_cost = max(mst_edges, key=lambda x: x[2])[2]
    # 최소 스패닝 트리 비용에서 가장 비용이 큰 간선을 제거
    return mst_cost - max_edge_cost


import sys
input = sys.stdin.readline
N, M = map(int, input().split())
roads = []
for _ in range(M):
    h1, h2, c = map(int, input().split())
    roads.append((h1, h2, c))
print(solution(N, M, roads))