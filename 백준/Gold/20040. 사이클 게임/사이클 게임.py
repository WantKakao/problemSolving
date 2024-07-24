class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1] * n

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)
        if root_u != root_v:
            if self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            elif self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            else:
                self.parent[root_v] = root_u
                self.rank[root_u] += 1
            return False
        return True


import sys
input = sys.stdin.readline

dot, turn = map(int, input().split())
edges = []
for _ in range(turn):
    edges.append([*map(int, input().split())])

# Union-Find 초기화
uf = UnionFind(dot)  # 노드 번호가 0부터 시작한다

# 사이클 판별
has_cycle = False
for i in range(turn):
    u, v = edges[i][0], edges[i][1]
    if uf.union(u, v):
        has_cycle = True
        break

if has_cycle:
    print(i+1)
else:
    print(0)


