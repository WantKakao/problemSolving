n = int(input())
i = 0
while True:
    if n <= 2**i:
        n -= 2**(i-1)
        break
    i += 1

k = 1
while 2**(i-1) > n > 0:
    if n >= 2**(i-k):
        n -= 2**(i-k)
    k += 1


print(2**i, k-1)