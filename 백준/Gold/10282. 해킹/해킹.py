from collections import deque
import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, d, c = map(int, input().split())
    computer = [[] for _ in range(n+1)]
    q = deque()
    virus = [-1 for _ in range(n+1)]

    for _ in range(d):
        a, b, s = map(int, input().split())
        computer[b].append([a, s])

    for end, cost in computer[c]:
        q.append((end, cost))
        virus[end] = cost

    while q:
        start, cost = q.popleft()
        for end, cost2 in computer[start]:
            total_cost = cost + cost2
            if virus[end] == -1 or total_cost < virus[end]:
                virus[end] = total_cost
                q.append((end, total_cost))

    cnt = 0
    M = 0
    for i in range(1, n+1):
        if i != c and virus[i] != -1:
            cnt += 1
            if virus[i] > M:
                M = virus[i]

    print(cnt+1, M)