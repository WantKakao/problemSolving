import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

n, m, r = map(int, input().split())
g = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)
for i in range(n+1):
    g[i].sort()

visited = [0 for _ in range(n+1)]
answer = [0 for _ in range(n+1)]
a = 1
def dfs(r):
    global  a
    visited[r] = 1
    answer[r] = a
    a += 1
    for j in g[r]:
        if not visited[j]:
            dfs(j)

dfs(r)
for k in range(1, n+1):
    print(answer[k])