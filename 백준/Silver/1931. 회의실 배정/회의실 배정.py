import sys
input = sys.stdin.readline

time_table = []
n = int(input())
for _ in range(n):
    start, end = map(int, input().split())
    time_table.append((end, start))
time_table.sort()

temp = 0
ans = 0
for e, s in time_table:
    if s >= temp:
        ans += 1
        temp = e
print(ans)