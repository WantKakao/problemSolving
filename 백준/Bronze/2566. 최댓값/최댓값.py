l = []
for _ in range(9):
    l.append(list(map(int, input().split())))
M = -1
x, y = 0, 0
for i in range(9):
    for j in range(9):
        if l[i][j] > M:
            M = l[i][j]
            x, y = i+1, j+1
            
print(M)
print(x, y)