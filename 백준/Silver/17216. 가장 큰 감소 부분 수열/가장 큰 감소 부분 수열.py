# 17216 가장 큰 감소 부분 수열
n = int(input())
nums = list(map(int, input().split()))

dp = [nums[i] for i in range(n)]
for i in range(n):
    for j in range(i):
        if nums[i] < nums[j]:
            dp[i] = max(dp[i], dp[j]+nums[i])

print(max(dp))