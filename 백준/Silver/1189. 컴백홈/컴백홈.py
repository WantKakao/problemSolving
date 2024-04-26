r, c, k = map(int, input().split())
arr = []
for _ in range(r):
    arr.append([*map(str, input().rstrip())])

visited = [[False for _ in range(c)] for _ in range(r)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
ans = 0


def dfs(x, y, d):
    global ans, k
    visited[x][y] = True
    if d == k:
        if x == 0 and y == c-1:
            ans += 1
        return

    for t in range(4):
        nx = x + dx[t]
        ny = y + dy[t]
        if 0 <= nx < r and 0 <= ny < c and arr[nx][ny] == '.' and not visited[nx][ny]:
            dfs(nx, ny, d+1)
            visited[nx][ny] = False


dfs(r-1, 0, 1)
print(ans)