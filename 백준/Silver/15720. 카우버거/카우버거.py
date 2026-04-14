b, c, d = map(int, input().split())
bl = list(map(int, input().split()))
cl = list(map(int, input().split()))
dl = list(map(int, input().split()))
bl.sort(reverse=True)
cl.sort(reverse=True)
dl.sort(reverse=True)
m = min(b, c, d)
ans = 0
for i in range(m):
    ans += bl[i]
    ans += cl[i]
    ans += dl[i]
s = sum(bl) + sum(cl) + sum(dl)
print(s)
print(s - (ans // 10))