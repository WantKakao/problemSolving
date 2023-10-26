n = int(input())
houses = []
for _ in range(n):
    houses.append([*map(int, input().rstrip())])
visited = [[False for _ in range(n)] for _ in range(n)]
ans = 0
d = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def dfs(x, y):
    global count
    visited[x][y] = True
    for i in range(4):
        new_x = x + d[i][0]
        new_y = y + d[i][1]
        if new_x >= 0 and new_y >= 0 and new_x < n and new_y < n and not visited[new_x][new_y]:
            if houses[new_x][new_y] == 1:
                count += 1
                dfs(new_x, new_y)
    return


counts = []
for i in range(n):
    for j in range(n):
        if not visited[i][j] and houses[i][j] == 1:
            count = 1
            ans += 1
            dfs(i, j)
            counts.append(count)

print(ans)
counts.sort()
for c in counts:
    print(c)