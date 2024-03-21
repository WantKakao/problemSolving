from collections import deque
import sys
input = sys.stdin.readline

ans = 0
gear = [[0]]
for _ in range(4):
    q = deque(input().rstrip())
    gear.append(q)
n = int(input())
q = deque()

for _ in range(n):
    g, d = map(int, input().split())
    q.append((g, d))
    visited = [0 for _ in range(5)]
    while q:
        g, d = q.popleft()
        visited[g] = 1
        ng = g + 1
        pg = g - 1
        if ng <= 4 and gear[g][2] != gear[ng][6] and not visited[ng]:
            q.append((ng, -d))
        if 0 < pg and gear[g][6] != gear[pg][2] and not visited[pg]:
            q.append((pg, -d))
        if d == 1:
            t = gear[g].pop()
            gear[g].appendleft(t)
        else:
            t = gear[g].popleft()
            gear[g].append(t)

for i in range(5):
    if gear[i][0] == '1':
        ans += 2**(i-1)
print(ans)
