m, n = map(int, input().split())
k = int(input())
i, j = 1, n
ans = 0
for _ in range(k):
    x = int(input())
    if i <= x <= j:
        continue
    elif x < i:
        t = (i-x)
        ans += t
        i -= t
        j -= t
    else:
        t = (x-j)
        ans += t
        i += t
        j += t
print(ans)