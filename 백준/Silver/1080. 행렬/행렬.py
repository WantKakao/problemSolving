n, m = map(int, input().split())
A, B = [], []
for _ in range(n):
    A.append(list(map(int, input())))
for _ in range(n):
    B.append(list(map(int, input())))

ans = 0
fail = False
if (n < 3 or m < 3) and A != B:
    fail = True
    
def flip(M, x, y):
    for i in range(3):
        for j in range(3):
            if M[x+i][y+j] == 0:
                M[x+i][y+j] = 1
            else:
                M[x+i][y+j] = 0
    
for i in range(n-2):
    for j in range(m-2):
        if A[i][j] != B[i][j]:
            flip(A, i, j)
            ans += 1
    if A[i][m-2] != B[i][m-2] or A[i][m-1] != B[i][m-1]:
        fail = True
        
if A != B:
    fail = True

if fail:
    print(-1)
else:
    print(ans)