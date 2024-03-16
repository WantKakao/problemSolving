import sys
input = sys.stdin.readline

n = int(input())
graph = []
for _ in range(n):
    graph.append([*map(int, input().split())])
ans = 1e9


def dfs(i, t1, c):
    global ans
    t1.append(i)
    c += 1
    if c == n//2:
        a, b = 0, 0
        t2 = []
        for j in range(n):
            if j not in t1:
                t2.append(j)
        for t in t1:
            for tt in t1:
                a += graph[t][tt]
        for s in t2:
            for ss in t2:
                b += graph[s][ss]
        if abs(a-b) < ans:
            ans = abs(a-b)
    else:
        for k in range(i+1, n):
            dfs(k, t1, c)
    t1.remove(i)

for p in range(n//2):
    dfs(p, [], 0)

print(ans)