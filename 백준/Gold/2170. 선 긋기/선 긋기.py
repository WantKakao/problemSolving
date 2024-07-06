import sys
input = sys.stdin.readline

n = int(input())
line = []
for _ in range(n):
    start, end = map(int, input().split())
    line.append((start, end))

line.sort()
s, e = line[0][0], line[0][1]
ans = 0
for i in range(1, n):
    if e >= line[i][0]:
        e = max(e, line[i][1])
    else:
        ans += e-s
        s = line[i][0]
        e = line[i][1]
ans += e-s
print(ans)