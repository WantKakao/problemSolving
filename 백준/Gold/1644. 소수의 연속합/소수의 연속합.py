n = int(input())

is_prime = [True for _ in range(n+1)]
prime_number = []
for i in range(2, n+1):
    if is_prime[i]:
        prime_number.append(i)
        for j in range(i, n+1, i):
            is_prime[j] = False

p = len(prime_number)
ans = 0
i, j = 0, 1
temp = 2
while i <= j <= p:
    if n == temp:
        ans += 1
        if j < p:
            temp += prime_number[j]
        if i < p:
            temp -= prime_number[i]
        i += 1
        j += 1
    elif n > temp:
        if j < p:
            temp += prime_number[j]
        j += 1
    elif i < p:
        if i < p:
            temp -= prime_number[i]
        i += 1

print(ans)