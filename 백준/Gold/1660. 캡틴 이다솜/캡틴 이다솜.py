n = int(input())

i = 1
num = 0
nums = [0]
while nums[-1] <= n:
    num += i
    nums.append(nums[-1] + num)
    i += 1

INF = int(1e9)
dp = [INF] * (n+1)
dp[0] = 0

for c in nums:  # 사용할 수 있는 수
    for x in range(c, n+1):
        dp[x] = min(dp[x], dp[x-c] + 1)

print(dp[n])