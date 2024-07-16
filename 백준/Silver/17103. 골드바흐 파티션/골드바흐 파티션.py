import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    is_prime = [True for _ in range(n+1)]
    prime = []
    for i in range(2, n+1):
        if is_prime[i]:
            prime.append(i)
            for j in range(i, n+1, i):
                is_prime[j] = False

    a = 0
    b = len(prime) - 1
    ans = 0
    while a <= b:
        if prime[a] + prime[b] == n:
            ans += 1
            a += 1
            b -= 1
        elif prime[a] + prime[b] > n:
            b -= 1
        else:
            a += 1

    print(ans)