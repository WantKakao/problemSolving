t = int(input())
for _ in range(t):
    ans = int(input())
    n = int(input())
    for _ in range(n):
        a, b = map(int, input().split())
        ans += a*b
    print(ans)