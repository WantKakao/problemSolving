l = [0, -1, 1, -1, 2, 1, 3, 2, 4, 3]
n = int(input())
a, b = divmod(n, 10)
if l[b] != -1:
    ans = a*2 + l[b]
    print(ans)
else:
    if a > 0:
        ans = a*2 + l[b+5] - 1
        print(ans)
    else:
        print(-1)