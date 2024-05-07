n = int(input())

dp = [1e9 for _ in range(n+1)]
command = [0 for _ in range(n+1)]
dp[1] = 0

for i in range(1, n+1):
    if i+1 <= n:
        if dp[i]+1 < dp[i+1]:
            dp[i+1] = dp[i]+1
            command[i+1] = 1

    if 2*i <= n:
        if dp[i]+1 < dp[2*i]:
            dp[2*i] = dp[i] + 1
            command[2*i] = 2

    if 3*i <= n:
        if dp[i]+1 < dp[3*i]:
            dp[3*i] = dp[i] + 1
            command[3*i] = 3

print(dp[n])
print(n, end=' ')
while n != 1:
    if command[n] == 1:
        n -= 1
    elif command[n] == 2:
        n //= 2
    else:
        n //= 3
    print(n, end=' ')