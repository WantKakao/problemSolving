from collections import Counter

S = input()
N = int(input())
words = []
for _ in range(N):
    words.append(input())

s = len(S)
possible = [False for _ in range(s+1)]
possible[0] = True
dp = [s for _ in range(s+1)]
for i in range(s):
    if possible[i] == True:
        for j in range(N):
            w = len(words[j])
            if w <= s-i and Counter(words[j]) == Counter(S[i:i+w]):
                possible[i+w] = True
                temp = 0
                for k in range(w):
                    if words[j][k] == S[i+k]:
                        temp += 1
                dp[i+w] = min(dp[i+w], dp[i]-temp)

ans = dp[s] if possible[s] == True else -1
print(ans)