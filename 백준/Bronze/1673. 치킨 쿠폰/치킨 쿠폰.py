while True:
    try:
        n, k = map(int, input().split())
        ans = n
        while n >= k:
            a, b = divmod(n, k)
            ans += a
            n = a + b
        print(ans)
    except EOFError:
        break