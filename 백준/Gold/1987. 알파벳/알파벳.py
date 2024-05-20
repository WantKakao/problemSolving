import sys
sys = sys.stdin.readline

r, c = map(int, input().split())
alphabet = []
for _ in range(r):
    alphabet.append([*map(str, input().rstrip())])

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
max_depth = 0


def dfs(x, y, arr):
    global max_depth

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < r and 0 <= ny < c and alphabet[nx][ny] not in arr:
            dfs(nx, ny, arr + alphabet[nx][ny])

    if len(arr) > max_depth:
        max_depth = len(arr)


dfs(0, 0, alphabet[0][0])
print(max_depth)