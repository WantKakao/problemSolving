n, m = map(int, input().split())
l = [i for i in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    l[a:b+1] = l[b:a-1:-1]
for i in range(1, n+1):
    print(l[i], end=' ')