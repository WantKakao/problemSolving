t = int(input())
for _ in range(t):
    arr = [*map(int, input().split())]
    arr.sort()
    m = 0
    s = 0
    for a in arr:
        if a % 2 == 0:
            s += a
            if m == 0:
                m = a
    print(s, m)