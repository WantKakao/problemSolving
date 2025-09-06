from collections import deque

n = int(input())
bridge = [0] + list(map(int, input().split()))
a, b = map(int, input().split())

visited = [False for _ in range(n+1)]
visited[a] = True
jump = [-1 for _ in range(n+1)]
jump[a] = 0
q = deque()
q.append((a, jump[a]))
while q:
    t, d = q.popleft()
    for i in range(t, n+1, bridge[t]):
        if not visited[i]:
            jump[i] = d+1
            q.append((i, d+1))
            visited[i] = True
    for i in range(t, 0, -bridge[t]):
        if not visited[i]:
            jump[i] = d+1
            q.append((i, d+1))
            visited[i] = True
            
print(jump[b])