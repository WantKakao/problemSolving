n = int(input())
l = list(map(int, input().split()))

l.sort()
t = 0
ans = 0
l2 = []
for i in range(n):
    if l[i] > t:
        ans += 1
        t = l[i]
    else:
        l2.append(l[i])
l2.sort()
t = 0
for i in range(0, len(l2)):
    if l2[i] > t:
        ans += 1
        t = l2[i]
print(ans)