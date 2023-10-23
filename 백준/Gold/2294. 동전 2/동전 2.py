import sys
input = sys.stdin.readline

coin, value = map(int, input().split())
coins = []
for _ in range(coin):
    coins.append(int(input()))
coins.sort()
# print(coins)
INF = 10e5
ans = [INF for _ in range(value+1)]
for c in coins:
    if c <= value:
        ans[c] = 1

for i in range(coins[0]+1, value+1):
    for c in coins:
        if i-c >= 1:
            ans[i] = min(ans[i], ans[i-c]+1)
if ans[-1] == INF:
    print(-1)
else:
    print(ans[-1])