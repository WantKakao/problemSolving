import sys
import heapq
from collections import deque

input = sys.stdin.readline
n = int(input())
q = []
for i in range(n):
    num, start, end = map(int, input().split())
    heapq.heappush(q, (start, end, num))

start, end, num = heapq.heappop(q)
arr = [(end, 1)]
ans = 1
order = [0 for _ in range(n+1)]
order[num] = 1

while q:
    start, end, num = heapq.heappop(q)
    if start >= arr[0][0]:
        e, t = heapq.heappop(arr)
        heapq.heappush(arr, (end, t))
        order[num] = t
    else:
        ans += 1
        heapq.heappush(arr, (end, ans))
        order[num] = ans

print(ans)
for i in order[1:]:
    print(i)