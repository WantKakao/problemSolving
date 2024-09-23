t = int(input())
for _ in range(t):
    n = int(input())
    p = list(map(int, input().split()))
    p.sort()
    m = (p[-1] + p[0]) // 2
    val = p[0]
    for i in range(n):
        if abs(m - p[i]) < abs(m - val):
            val = p[i]
    print((abs(val - p[0]) + abs(val - p[-1])) * 2)