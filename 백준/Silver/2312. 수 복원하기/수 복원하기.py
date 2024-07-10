import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())

    prime = []
    is_prime = [1 for _ in range(n+1)]
    for i in range(2, n+1):
        if is_prime[i] == 1:
            prime.append(i)
            for j in range(2*i, n+1, i):
                is_prime[j] = 0

    p = len(prime)
    count = [0 for _ in range(p)]
    for i in range(p):
        while n % prime[i] == 0:
            n //= prime[i]
            count[i] += 1
        if n == 1:
            break

    for i in range(p):
        if count[i] != 0:
            print(prime[i], count[i])
