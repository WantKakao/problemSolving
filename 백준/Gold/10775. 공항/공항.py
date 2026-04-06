import sys
input = sys.stdin.readline

g = int(input())
p = int(input())

parent = list(range(g+1))

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

count = 0

for _ in range(p):
    plane = int(input())
    root = find(plane)
    
    if root == 0:
        break
    
    parent[root] = find(root-1)
    count += 1

print(count)
