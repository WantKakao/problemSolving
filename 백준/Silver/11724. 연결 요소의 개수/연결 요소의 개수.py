import sys
input = sys.stdin.readline

v, e = map(int, input().split())
conncection = []

for _ in range(e):
    i, j = map(int, input().split())
    conncection.append((i, j))

# print(conncection)
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

while conncection:
    x, y = conncection.pop()
    union(x, y)

for i in range(len(parent)):
    parent[i] = find_parent(i)

p = []
count = 0
for i in parent:
    if i not in p:
        count += 1
        p.append(i)

print(count-1)