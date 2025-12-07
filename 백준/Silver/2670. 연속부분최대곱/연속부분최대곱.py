import sys
input = sys.stdin.readline

n = int(input())
ans = 1
M = 0
l = []
for _ in range(n):
    l.append(float(input()))

for i in range(n):
    ans *= l[i]
    if ans < 1:
        ans = 1
    M = max(M, ans)
    
M = M if max(l) >= 1 else max(l)
print("%.3f"%M)