import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
a, b = [], []
for _ in range(n):
    a.append(int(input()))
for _ in range(m):
    b.append(int(input()))
p = min(sum(a), sum(b))
ans = 0
a1, b1 = p, p
i = 0
while i < n and a1 > 0:
    if a1 - a[i] >= 0:
        ans += ((i+1)*a[i])
        a1 -= a[i]
    else:
        ans += ((i+1)*(a1))
        a1 = 0
    i += 1
i = 0
while i < m and b1 > 0:
    if b1 - b[i] >= 0:
        ans += ((i+1)*b[i])
        b1 -= b[i]
    else:
        ans += ((i+1)*(b1))
        b1 = 0
    i += 1
print(p, ans)