import sys

n = int(input())
arr = [*map(int, sys.stdin.readline().split())]

dp = [1 for _ in range(n)]
for i in range(n):
    m, M = 0, arr[i]
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j] + 1)
print(max(dp))