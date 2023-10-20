import sys
input = sys.stdin.readline
import heapq

v, e = map(int, input().split())
edge = []
ans = 0
parent = [i for i in range(v+1)]

for _ in range(e):
    i, j, c = map(int, input().split())
    heapq.heappush(edge, (c, i, j))


def find_parent(x):
    if parent[x] == x:
        return x
    else:
        parent[x] = find_parent(parent[x])
        return parent[x]


def union(x, y):
    a = find_parent(x)
    b = find_parent(y)
    if a > b:
        parent[a] = b
    else:
        parent[b] = a


while edge:
    c, i, j = heapq.heappop(edge)
    find_parent(i)
    find_parent(j)
    if parent[i] == parent[j]:
        continue
    else:
        union(i, j)
        ans += c

print(ans)