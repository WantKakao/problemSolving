s1 = input()
s2 = input()
dp = [[0 for _ in range(len(s2))] for _ in range(len(s1))]

for i in range(len(s1)):
    if s2[0] == s1[i]:
        dp[i][0] = 1
for j in range(len(s2)):
    if s1[0] == s2[j]:
        dp[0][j] = 1

for i in range(1, len(s1)):
    for j in range(1, len(s2)):
        if s1[i] == s2[j]:
            dp[i][j] = max(dp[i-1][j-1]+1, dp[i][j])
    
print(max(map(max, dp)))