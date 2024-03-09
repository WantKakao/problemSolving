n, m = map(int, input().split())
r, c, d = map(int, input().split())
room = []
for _ in range(n):
    room.append([*map(int, input().split())])
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
ans = 1


def clean(x, y):
    global ans, d
    room[x][y] = 2
    cnt = 0
    while True:
        d = (d-1) % 4
        nx, ny = x + dx[d], y + dy[d]
        if 0 <= nx < n and 0 <= ny < m and room[nx][ny] == 0:
            x, y = nx, ny
            ans += 1
            room[x][y] = 2
            cnt = 0
        else:
            cnt += 1
        if cnt == 4:
            mx, my = x + dx[(d+2)%4], y + dy[(d+2)%4]
            if 0 <= mx < n and 0 <= my < m and room[mx][my] == 2:
                x, y = mx, my
                cnt = 0
            else:
                break


clean(r, c)
print(ans)