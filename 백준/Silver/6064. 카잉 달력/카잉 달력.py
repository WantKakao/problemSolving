t = int(input())
for _ in range(t):
    M, N, x, y = map(int, input().split())

    m, n = M, N
    while n:
        m, n = n, m % n
    limit = abs(M * N) // m

    found = False
    nums = [i for i in range(x, limit+1, M)]
    for num in nums:
        if num % N == y % N:
            print(num)
            found = True
            break

    if not found:
        print(-1)