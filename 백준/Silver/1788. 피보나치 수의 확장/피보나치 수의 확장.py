n = int(input())

fibo = [0, 1, 1]
if n == 0:
    print(0)
    print(0)

elif abs(n) <= 2:
    if n % 2 == 0 and n < 0:
        print(-1)
    else:
        print(1)
    print(fibo[abs(n)])

else:
    for _ in range(abs(n)-2):
        fibo[0] = fibo[1]
        fibo[1] = fibo[2]
        fibo[2] = (fibo[0] + fibo[1]) % 1000000000
    if n % 2 == 0 and n < 0:
        print(-1)
    else:
        print(1)
    print(fibo[2])