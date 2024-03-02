import sys
sys.setrecursionlimit(1000000)

n, m = map(int, input().split())
canvas = []
for _ in range(n):
    canvas.append([*map(int, input().split())])


def bfs(x, y):
    global b
    canvas[x][y] = 0
    b += 1
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    for i in range(4):
        if x+dx[i] >= 0 and x+dx[i] < n and y+dy[i] >= 0 and y+dy[i] < m:
            if canvas[x+dx[i]][y+dy[i]] == 1:
                bfs(x+dx[i], y+dy[i])


answer = 0
B = 0
for i in range(n):
    for j in range(m):
        if canvas[i][j] == 1:
            answer += 1
            b = 0
            bfs(i, j)
            if B < b:
                B = b

print(answer)
print(B)