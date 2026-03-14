n = int(input())
i, j = 1, 1
t = 0
ans = 0
while j <= n+1:
    if t < n:
        t += j
        j += 1
    elif t > n:
        t -= i
        i += 1
    else:
        ans += 1
        t -= i
        i += 1
print(ans)