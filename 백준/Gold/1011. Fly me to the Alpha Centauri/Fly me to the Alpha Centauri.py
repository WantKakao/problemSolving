import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    n = b - a
    s, e = 0, 2**16
    while s <= e:
        m = (s+e) // 2
        S = m * (m+1) - m
        if S >= n:
            if S - m >= n:
                ans = 2 * m - 2
            else:
                ans = 2 * m - 1
            e = m - 1
        elif S < n:
            s = m + 1

    print(ans)
