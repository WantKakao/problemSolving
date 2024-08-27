
s1 = input()
s2 = input()
s3 = input()

dp = [[[0 for _ in range(len(s3))] for _ in range(len(s2))] for _ in range(len(s1))]

for i in range(len(s1)):
    for j in range(len(s2)):
        for k in range(len(s3)):
            if s1[i] == s2[j] == s3[k]:
                if i == 0 or j == 0 or k == 0:
                    dp[i][j][k] = 1
                else:
                    dp[i][j][k] = dp[i-1][j-1][k-1] + 1
            else:
                dp[i][j][k] = max(dp[i-1][j][k], dp[i][j-1][k], dp[i][j][k-1])

print(dp[len(s1)-1][len(s2)-1][len(s3)-1])