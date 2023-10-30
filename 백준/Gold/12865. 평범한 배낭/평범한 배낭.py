import sys
n, k = map(int, sys.stdin.readline().split())
items = [0]
for _ in range(n):
    items.append([*map(int, input().split())])      # items = [[0], [weight, value], ..., ]
dp = [0 for _ in range(k+1)]

for i in range(1, n+1):
    for j in range(k, 0, -1):
        if j >= items[i][0]:
            dp[j] = max(dp[j], dp[j-items[i][0]]+items[i][1])
print(dp[-1])