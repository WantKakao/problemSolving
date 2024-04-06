n, m = map(int, input().split())
route = []
for _ in range(n):
    route.append(list(map(int, input().split())))

i = 0
M = 1000
d = [-1, 0, 1]


def findRoute(x, y, dir, temp):
    global M
    if temp >= M:
        return
    if x == n-1:
        M = temp
        return
    for i in range(3):
        if i == dir:
            continue
        ny = y + d[i]
        if 0 <= ny < m:
            findRoute(x+1, ny, i, temp + route[x+1][ny])


for j in range(m):
    findRoute(0, j, -1, route[0][j])
print(M)