import sys
input = sys.stdin.readline

v = int(input())
e = int(input())
network = []
for _ in range(e):
    i, j = map(int, input().split())
    network.append((i, j))

# print(network)
parent = [i for i in range(v+1)]
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

while network:
    x, y = network.pop()
    union(x, y)

# print(parent)
for i in range(len(parent)):
    parent[i] = find_parent(i)

ans = -1
for i in parent:
    if i == 1:
        ans += 1

print(ans)