import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

n, l, r = map(int, input().split())
nation = []
for _ in range(n):
    nation.append(list(map(int, input().split())))

Day = 0
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    global temp_sum
    visited[x][y] = True
    temp.append((x, y))
    temp_sum += nation[x][y]
    for d in range(4):
        nx, ny = x + dx[d], y + dy[d]
        if (0 <= nx < n and 0 <= ny < n and not visited[nx][ny]
                and l <= abs(nation[x][y] - nation[nx][ny]) <= r):
            bfs(nx, ny)


while True:
    visited = [[False for _ in range(n)] for _ in range(n)]
    count = 0
    for i in range(n):
        for j in range(n):
            temp = []
            temp_sum = 0
            if not visited[i][j]:
                count += 1
                bfs(i, j)
                for x, y in temp:
                    nation[x][y] = temp_sum // len(temp)

    if count == n ** 2:
        break
    else:
        Day += 1

print(Day)