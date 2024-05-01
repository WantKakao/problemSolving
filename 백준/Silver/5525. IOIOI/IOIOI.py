n = int(input())
m = int(input())
S = input()

Pn = "IO"*n + "I"
p = len(Pn)
ans = 0
i, j = 0, 0
while i+j < m:
    if S[i+j] == Pn[j]:
        j += 1
        if j == p:
            ans += 1
            j -= 2
            i += 2
    else:
        if S[i+j] == "I":
            i = i+j
        else:
            i = i+j+1
        j = 0

print(ans)