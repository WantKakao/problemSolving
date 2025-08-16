A, B = map(int, input().split())

is_prime = [True for _ in range(50000)]
is_prime[0], is_prime[1] = False, False
for n in range(2, 50000):
    if is_prime[n]:
        for k in range(n*2, 50000, n):
            if is_prime[k]:
                is_prime[k] = False

prime = [i for i in range(50000) if is_prime[i]]
ans = 0
for num in range(A, B+1):
    temp = 0
    for p in prime:
        if num < p:
            break
        while num % p == 0:
            temp += 1
            num //= p
    if is_prime[temp]:
        ans += 1
print(ans)