import sys
input = sys.stdin.readline

n = int(input())
minus = []
plus = []
one = []
for _ in range(n):
    k = int(input())
    if k <= 0:
        minus.append(k)
    elif k == 1:
        one.append(k)
    else:
        plus.append(k)

minus.sort()
plus.sort(reverse=True)

ans = len(one)
for i in range(0, len(plus), 2):
    if i+1 < len(plus):
        ans += (plus[i]*plus[i+1])
    else:
        ans += plus[i]
for j in range(0, len(minus), 2):
    if j+1 < len(minus):
        ans += (minus[j]*minus[j+1])
    else:
        ans += minus[j]

print(ans)