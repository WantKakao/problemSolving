l = []
s = ''
for _ in range(5):
    l.append(list(str(input().rstrip())))
M = 0
for i in range(5):
    M = max(M, len(l[i]))
for j in range(M):
    for i in range(5):
        if len(l[i]) > j:
            s += l[i][j]
print(s)