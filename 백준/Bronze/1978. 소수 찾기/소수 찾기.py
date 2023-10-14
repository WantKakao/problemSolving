p = int(input())
is_prime = list(map(int, input().split()))
primes = 0

for num in is_prime:
    count = 0
    for divisor in range(1, num):
        if divisor == num-1:
            primes += 1
        if num % divisor == 0 and divisor != 1:
            count += 1
        if count != 0:
            break
            
print(primes)