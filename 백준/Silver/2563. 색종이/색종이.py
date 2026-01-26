n = int(input())
l = [[0 for _ in range(100)] for _ in range(100)]
for _ in range(n):
    a, b = map(int, input().split())
    for i in range(a-1, a+9):
        for j in range(b-1, b+9):
            l[i][j] = 1
c = 0
for i in range(100):
    for j in range(100):
        if l[i][j] == 1:
            c += 1
print(c)