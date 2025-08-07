L = int(input())
S = list(map(int, input().split()))
n = int(input())

S.sort()
x = 0
ans = 1
for i in range(L):
    if  S[i] == n:
        ans = 0
        break
    if S[i] > n:
        x = i
        break

if x == 0:
    a, b = 0, S[x]
    
else:
    a, b = S[x-1], S[x]

if ans:
    ans = (n - a) * (b - n) - 1
print(ans)