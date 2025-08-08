X, Y = map(int, input().split())
p = (Y * 100) // X

if p >= 99:
    print(-1)
else:
    lo, hi = 1, 1_000_000_000
    ans = -1
    while lo <= hi:
        mid = (lo + hi) // 2
        new_p = ((Y + mid) * 100) // (X + mid)
        if new_p > p:
            ans = mid
            hi = mid - 1
        else:
            lo = mid + 1
    print(ans)
