n, m = map(int, input().split())
table = []
for _ in range(n):
    table.append(list(map(int, input())))
k = int(input())

ans = 0
for i in range(n):
    zeros = [j for j in range(m) if table[i][j] == 0]
    z = len(zeros)
    temp = 0
    if z <= k and (k-z) % 2 == 0:
        for i2 in range(n):
            if all(table[i2][j] == 0 for j in zeros) and table[i2].count(0) == z:
                temp += 1
        ans = max(ans, temp)

print(ans)