L, R = input().split()
while len(L) < len(R):
    L = '0' + L
    
ans = 0
for i in range(len(L)):
    if L[i] == R[i] == '8':
        ans += 1
    elif L[i] != R[i]:
        break
print(ans)