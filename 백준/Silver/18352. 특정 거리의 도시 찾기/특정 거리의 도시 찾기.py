import sys
input = sys.stdin.readline
from collections import deque

v, e, d, s = map(int, input().split())
road = [[] for _ in range(v+1)]
for _ in range(e):
    i, j = map(int, input().split())
    road[i].append(j)

q = deque()
visited = [False for _ in range(v+1)]
ans = []
def bfs(x):
    # global ans
    q.append((x, 0))
    visited[x] = True
    while q:
        t, c = q.popleft()
        if c == d:
            ans.append(t)
        if c > d:
            break
        for i in road[t]:
            if visited[i] == False:
                q.append((i, c+1))
                visited[i] = True

bfs(s)
ans.sort()
if not ans:
    print(-1)
else:
    for i in ans:
        print(i)