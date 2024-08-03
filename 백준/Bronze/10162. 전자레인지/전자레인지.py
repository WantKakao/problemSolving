n = int(input())
A, B, C = 300, 60, 10
a, b, c = 0, 0, 0

if n % 10 != 0:
    print(-1)
else:
    if n >= A:
        a += n//A
        n %= A
    if n >= B:
        b += n//B
        n %= B
    c += n//C

    print(a, b, c)
