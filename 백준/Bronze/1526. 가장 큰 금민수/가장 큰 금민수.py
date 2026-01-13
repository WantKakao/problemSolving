n = int(input())
for i in range(n, 3, -1):
    s = str(i)
    f = True
    for k in s:
        if k not in ['4', '7']:
            f = False
    if f:
        print(i)
        break