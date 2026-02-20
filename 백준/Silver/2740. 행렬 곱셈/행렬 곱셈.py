n, m = map(int, input().split())
a1 = []
for _ in range(n):
    a1.append(list(map(int, input().split())))
n2, m2 = map(int, input().split())
a2 = []
for _ in range(n2):
    a2.append(list(map(int, input().split())))

a = [[0 for _ in range(m2)] for _ in range(n)]
for i in range(n):
    for j in range(m2):
        for k in range(m):
            a[i][j] += (a1[i][k]*a2[k][j])
            
for i in range(n):
    for j in range(m2):
        print(a[i][j], end=' ')
    print()