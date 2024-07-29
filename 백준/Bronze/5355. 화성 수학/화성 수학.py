t = int(input())
for _ in range(t):
    op = list(map(str, input().split()))
    n = float(op[0])
    for i in range(1, len(op)):
        if op[i] == '@':
            n *= 3
        elif op[i] == '%':
            n += 5
        else:
            n -= 7
    print("{:.2f}".format(n))