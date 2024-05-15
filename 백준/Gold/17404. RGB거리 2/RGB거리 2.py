n = int(input())
house = []
for _ in range(n):
    house.append([*map(int, input().split())])

# dp_start[end]
dp0 = [2000, house[0][0]+house[1][1], house[0][0]+house[1][2]]
dp1 = [house[0][1]+house[1][0], 2000, house[0][1]+house[1][2]]
dp2 = [house[0][2]+house[1][0], house[0][2]+house[1][1], 2000]


def find_dp(dp, idx):
    for i in range(2, idx):
        temp0 = min(dp[1], dp[2]) + house[i][0]
        temp1 = min(dp[0], dp[2]) + house[i][1]
        temp2 = min(dp[0], dp[1]) + house[i][2]

        dp[0], dp[1], dp[2] = temp0, temp1, temp2
    return dp


result0 = find_dp(dp0, n)
result1 = find_dp(dp1, n)
result2 = find_dp(dp2, n)
new_result = [result0[1], result0[2], result1[0], result1[2], result2[0], result2[1]]

print(min(new_result))
