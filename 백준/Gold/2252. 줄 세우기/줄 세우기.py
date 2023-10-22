import sys
input = sys.stdin.readline
from collections import deque

v, e = map(int, input().split())
height = [[] for _ in range(v+1)]
degree = [0 for _ in range(v+1)]
for _ in range(e):
    a = [*map(int, input().split())]
    height[a[0]].append(a[1])
    degree[a[1]] += 1

zero_degree = []
q = deque()
result = []
for i in range(1, v+1):
    if degree[i] == 0:
        q.append(i)
        # result.append(i)
        print(i, end=' ')

while q:
    idx = q.popleft()
    for i in height[idx]:
        degree[i] -= 1
        if degree[i] == 0:
            q.append(i)
            # result.append(i)
            print(i, end=' ')