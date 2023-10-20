import sys
input = sys.stdin.readline
from collections import deque

v, e, s = map(int, input().split())
edge = [[] for _ in range(v+1)]
visited = [False for _ in range(v+1)]

for _ in range(e):
    i, j = map(int, input().split())
    edge[i].append(j)
    edge[j].append(i)
for x in range(1, v+1):
    edge[x].sort()

def dfs(x):
    if visited[x] == True:
        return
    visited[x] = True
    print(x, end=' ')
    for e in edge[x]:
        dfs(e)


dfs(s)
print()

visited = [False for _ in range(v+1)]
q = deque()

def bfs(x):
    q.append(x)
    while q:
        e = q.popleft()
        if visited[e] == False:
            visited[e] = True
            print(e, end=' ')
            for i in edge[e]:
                q.append(i)

bfs(s)