import sys
input = sys.stdin.readline
n, k = map(int, input().split())
coins = []
for _ in range(n):
    coins.append(int(input()))
cnt = 0
for i in reversed(coins):
    if i <= k:
        cnt += k // i
        k %= i
print(cnt)