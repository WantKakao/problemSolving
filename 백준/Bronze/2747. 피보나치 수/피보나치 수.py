n = int(input())
fibo = [0, 1, 1]
if n < 3:
    print(fibo[n])
else:
    for i in range(3, n+1):
        fibo.append(fibo[i-1] + fibo[i-2])
    print(fibo[n])