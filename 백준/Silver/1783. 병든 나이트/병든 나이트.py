n, m = map(int, input().split())
ans = 0
if n == 1 or m == 1:
    ans = 1
elif n == 2:
    if m >= 7:
        ans = 4
    else:
        ans = (m+1) // 2
else:
    if m == 2:
        ans = 2
    elif m == 3:
        ans = 3
    elif 4 <= m <= 6:
        ans = 4
    else:
        ans = (m-2)
print(ans)