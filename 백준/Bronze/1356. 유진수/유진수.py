s = input().rstrip()
ans = 'NO'
for i in range(1, len(s)):
    A = s[:i]
    B = s[i:]
    sumA = int(A[0])
    sumB = int(B[0])
    for a in range(1, len(A)):
        sumA *= int(A[a])
    for b in range(1, len(B)):
        sumB *= int(B[b])
    if sumA == sumB:
        ans = 'YES'
        break
        
print(ans)