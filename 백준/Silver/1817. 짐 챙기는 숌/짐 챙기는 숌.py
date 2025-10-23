n, m = map(int, input().split())
if n > 0:
    books = list(map(int, input().split()))
else:
    books = []
ans = 0
box = m
for b in books:
    if box + b <= m:
        box += b
    else:
        box = b
        ans += 1
print(ans)