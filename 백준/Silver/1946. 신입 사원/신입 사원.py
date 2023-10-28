import sys
input = sys.stdin.readline
import heapq

test = int(input())
for _ in range(test):
    n = int(input())
    grade = []
    for _ in range(n):
        x, y = map(int, input().split())
        heapq.heappush(grade, (x, y))
    m, cnt = n+1, 0
    while grade:
        a, b = heapq.heappop(grade)
        if b < m:
            m = b
            cnt += 1
    print(cnt)