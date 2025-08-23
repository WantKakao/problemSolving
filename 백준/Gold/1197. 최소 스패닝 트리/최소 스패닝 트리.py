import sys
input = sys.stdin.readline

def find(x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]  # 경로 압축
        x = parent[x]
    return x

def union(a, b):
    a, b = find(a), find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

V, E = map(int, input().split())
edges = []
for _ in range(E):
    u, v, w = map(int, input().split())
    edges.append((w, u, v))

edges.sort()
parent = [i for i in range(V+1)]

mst_cost = 0
for w, u, v in edges:
    if find(u) != find(v):
        union(u, v)
        mst_cost += w

print(mst_cost)
