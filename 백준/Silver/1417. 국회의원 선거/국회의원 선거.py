n = int(input())
t = int(input())
if n > 1:
    l = [int(input()) for _ in range(n-1)]
else:
    l = [0]
l.sort(reverse=True)
ans = 0
while t <= l[0]:
    l[0] -= 1
    ans += 1
    t += 1
    l.sort(reverse=True)
print(ans)