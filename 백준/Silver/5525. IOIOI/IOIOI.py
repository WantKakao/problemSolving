n = int(input())
m = int(input())
S = input()

Pn = "IO"*n + "I"
p = len(Pn)
ans = 0
for i in range(len(S)):
    if i+p <= m and S[i:i+p] == Pn:
        ans += 1

print(ans)