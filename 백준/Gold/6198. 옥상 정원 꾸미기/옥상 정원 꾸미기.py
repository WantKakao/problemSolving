from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
buildings = []
for _ in range(n):
    buildings.append(int(input()))

ans = 0
q = deque()
for i in range(n):
    while q and q[-1][1] <= buildings[i]:
        idx, height = q.pop()
        ans += i - idx - 1
    q.append((i, buildings[i]))

for idx, height in q:
    ans += n - idx - 1

print(ans)