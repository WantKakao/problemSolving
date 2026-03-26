n, k = map(int, input().split())
s = sum([i for i in range(1, k+1)])
if n < s:
    print(-1)
else:
    r = n - s
    if r % k == 0:
        print(k-1)
    else:
        print(k)