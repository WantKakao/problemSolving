t = int(input())
for _ in range(t):
    n = int(input())
    n2 = str(n * n)
    if n < 10:
        n2 = int(n2[-1:])
    elif n < 100:
        n2 = int(n2[-2:])
    elif n < 1000:
        n2 = int(n2[-3:])
    else:
        n2 = int(n2[-4:])
    if n2 == n:
        print('YES')
    else:
        print('NO')