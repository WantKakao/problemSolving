n, m = map(int, input().split())
l = [0 for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    l[a:b+1] = [c for _ in range(b-a+1)]
for i in range(1, n+1):
    print(l[i], end=' ')