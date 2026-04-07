a, k = map(int, input().split())
ans = 0
while (2*a) <= k:
    if k % 2 == 0:
        k //= 2
    else:
        k -= 1
    ans += 1
ans += (k-a)
print(ans)