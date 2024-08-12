# 6588 골드바흐의 추측
import sys
input = sys.stdin.readline

is_prime = [True for _ in range(1000000)]
prime = []
for i in range(2, 1000000):
    if is_prime[i]:
        prime.append(i)
        for j in range(2*i, 1000000, i):
            is_prime[j] = False

while True:
    n = int(input())
    if n == 0:
        break

    for p in prime:
        if is_prime[n-p]:
            print(f"{n} = {p} + {n-p}")
            break
