import bisect
n = int(input())
nums = list(map(int, input().split()))

dp = []
for num in nums:
    pos = bisect.bisect_left(dp, num)
    if pos < len(dp):
        dp[pos] = num
    else:
        dp.append(num)

print(len(dp))