arr = []
for _ in range(7):
    arr.append(int(input()))
m = 100
ans = 0
for a in arr:
    if a % 2 == 1:
        ans += a
        if a < m:
            m = a
if ans == 0:
    print(-1)
else:
    print(ans)
    print(m)