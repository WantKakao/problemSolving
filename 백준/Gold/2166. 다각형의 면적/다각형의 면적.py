import sys
input = sys.stdin.readline
n = int(input())
dots = []
for _ in range(n):
    dots.append([*map(int, input().split())])
ans = 0
x0, y0 = dots[0]
for i in range(1, n-1):
    x1, y1 = dots[i]
    x2, y2 = dots[i+1]
    temp = x0*y1 + x1*y2 + x2*y0 - x1*y0 - x2*y1 - x0*y2
    ans += temp/2
print(abs(ans))
