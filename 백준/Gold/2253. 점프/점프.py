import sys
input = sys.stdin.readline

n, m = map(int, input().split())
small_rock = []
for _ in range(m):
    small_rock.append(int(input()))

# print(small_rock)
k = round((2*n)**0.5)
# print(k)
INF = 1e9

dp = [[INF for _ in range(k+1)] for _ in range(n+1)]
dp[2][1] = 1
# print(dp)

for i in range(3, n+1):
    if i in small_rock:
        continue
    else:
        for j in range(1, k):
            dp[i][j] = min(dp[i-j][j-1] + 1, dp[i-j][j] + 1, dp[i-j][j+1] + 1)


# for i in dp:
#     print(i)
if min(dp[n]) >= INF or 2 in small_rock:
    print(-1)
else:
    print(min(dp[n]))