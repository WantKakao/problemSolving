s1 = input()
s2 = input()

dp = [[0 for _ in range(len(s2))] for _ in range(len(s1))]

if s1[0] == s2[0]:
    dp[0][0] = 1
for i in range(1, len(s1)):
    if s1[i] == s2[0]:
        dp[i][0] = 1
    else:
        dp[i][0] = dp[i-1][0]
for j in range(1, len(s2)):
    if s1[0] == s2[j]:
        dp[0][j] = 1
    else:
        dp[0][j] = dp[0][j-1]

for i in range(1, len(s1)):
    for j in range(1, len(s2)):
        if s1[i] == s2[j]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

print(dp[len(s1)-1][len(s2)-1])

LCS = []
i = len(s1)-1
j = len(s2)-1
while i >= 0 and j >= 0:
    if s1[i] == s2[j]:
        LCS.append(s1[i])
        i -= 1
        j -= 1
    elif i > 0 and dp[i][j] == dp[i-1][j]:
        i -= 1
    elif j > 0 and dp[i][j] == dp[i][j-1]:
        j -= 1
    else:
        break
LCS.reverse()

if LCS:
    print(''.join(LCS))