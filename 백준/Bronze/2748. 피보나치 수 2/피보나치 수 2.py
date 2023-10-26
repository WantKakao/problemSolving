n = int(input())
fibo = [0 for _ in range(91)]


def fibonacci(x):
    if x == 0:
        fibo[x] = 0
        return fibo[x]
    elif x == 1 or x == 2:
        fibo[x] = 1
        return fibo[x]
    elif fibo[x] != 0:
        return fibo[x]
    else:
        fibo[x] = fibonacci(x-1) + fibonacci(x-2)
    return fibo[x]

print(fibonacci(n))