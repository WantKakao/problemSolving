MAX = 100000

# 최소 소인수 (Smallest Prime Factor)
spf = [0] * (MAX+1)
for i in range(2, MAX+1):
    if spf[i] == 0:  # 소수라면
        for j in range(i, MAX+1, i):
            if spf[j] == 0:
                spf[j] = i

# 각 수의 소인수 개수
factor_cnt = [0] * (MAX+1)
for i in range(2, MAX+1):
    factor_cnt[i] = factor_cnt[i // spf[i]] + 1

# 소수 판별 (에라토스테네스)
is_prime = [True] * (MAX+1)
is_prime[0] = is_prime[1] = False
for i in range(2, int(MAX**0.5)+1):
    if is_prime[i]:
        for j in range(i*i, MAX+1, i):
            is_prime[j] = False

A, B = map(int, input().split())
ans = 0
for num in range(A, B+1):
    if is_prime[factor_cnt[num]]:
        ans += 1
print(ans)
