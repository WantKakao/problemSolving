n = int(input())
nums = list(map(int, input().split()))
k = int(input())

M = nums[-1]*k
dp = [k+1 for _ in range(M+2)]
for num in nums:
    dp[num] = 1

for i in range(1, M+2):
    if dp[i] == k+1:
        if i % 2 == 0:
            print(f"holsoon win at {i}")
        else:
            print(f"jjaksoon win at {i}")
        break
    for num in nums:
        dp[i+num] = min(dp[i+num], dp[i]+1)
        