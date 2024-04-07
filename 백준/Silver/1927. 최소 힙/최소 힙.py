import sys
input = sys.stdin.readline
import heapq

n = int(input())
q = []
for _ in range(n):
    op = int(input())
    if op == 0:
        if q:
            print(heapq.heappop(q))
        else:
            print(0)
    else:
        heapq.heappush(q, op)
