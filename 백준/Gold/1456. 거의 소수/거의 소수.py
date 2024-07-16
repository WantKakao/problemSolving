a, b = map(int, input().split())

is_prime = [True for _ in range(10000001)]
prime = []
for i in range(2, 10000001):
    if is_prime[i]:
        prime.append(i)
        for j in range(i, 10000001, i):
            is_prime[j] = False

almost_prime = []
for p in prime:
    ap = p * p
    while ap <= b:
        if a <= ap:
            almost_prime.append(ap)
        ap *= p

print(len(almost_prime))