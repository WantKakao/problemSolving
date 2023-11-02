n = int(input())
arr = [0] + [int(input()) for _ in range(n)]
# print(arr)
if n == 1:
    print(arr[n])
else:
    dp = [0 for _ in range(n+1)]
    dp[1], dp[2] = arr[1], arr[1] + arr[2]
    # 한칸 밟아서 도착시 그전에는 두칸이어야 함
    # 두칸 밟아서 도착시 그전에는 두칸이던 한칸이던 상관없음 -> 최대가 되려면 그전에 한칸?
    # dp[n] = arr[n-1] + dp[n-3]
    # dp[n] = arr[n-2] + max(dp[n-3], dp[n-4])
    for i in range(3, n+1):
        # 현재 + 한칸전 + 세칸전까지 vs 현재 + 두칸전까지
        dp[i] = max(arr[i] + arr[i-1] + dp[i-3], arr[i] + dp[i-2])
    print(dp[n])
