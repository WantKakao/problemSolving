import sys
input = sys.stdin.readline

n = int(input())
boxes = list(map(int, input().split()))

dp = [1 for _ in range(n)]
for i in range(n):
    for j in range(i+1, n):
        if boxes[i] < boxes[j]:
            dp[j] = max(dp[j], dp[i]+1)

print(max(dp))