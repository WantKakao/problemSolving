n = int(input())
l = [[0, 0] for _ in range(n+1)]
l[0] = [1, 0]

for i in range(1, n+1):
    l[i][0] = l[i-1][1]
    l[i][1] = l[i-1][0] + l[i-1][1]

print(l[n][0], l[n][1])