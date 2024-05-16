from collections import deque
import sys
input = sys.stdin.readline

N, Q = map(int, input().split())
USADO = [[0 for _ in range(N+1)] for _ in range(N+1)]
arr = [[] for _ in range(N+1)]
for _ in range(N-1):
    a, b, u = map(int, input().split())
    USADO[a][b], USADO[b][a] = u, u
    arr[a].append([b, u])
    arr[b].append([a, u])

for i in range(1, N+1):
    visited = [False for _ in range(N+1)]
    visited[i] = True
    q = deque([(i, 1e9)])
    while q:
        idx, cost = q.popleft()
        for d, c in arr[idx]:
            if not visited[d]:
                visited[d] = True
                USADO[i][d] = min(cost, c)
                q.append((d, USADO[i][d]))

for _ in range(Q):
    ans = 0
    usado, idx = map(int, input().split())
    for i in range(1, N+1):
        if USADO[idx][i] >= usado:
            ans += 1
    print(ans)