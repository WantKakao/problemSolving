n = int(input())
k = int(n**0.5 + 1)
prime = [2]
TF = [0 for _ in range(k+1)]

for i in range(3, k+1, 2):
    if TF[i] == 0:
        prime.append(i)
        for j in range(i, k+1, i):
            TF[j] = 1
    else:
        continue
p = 0

while n > 1 and p < len(prime):
    if n % prime[p] == 0:
        print(prime[p])
        n //= prime[p]
    else:
        p += 1

if n > 1:
    print(n)