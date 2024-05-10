n, m, x, y, k = map(int, input().split())
arr = []
for _ in range(n):
    arr.append([*map(int, input().split())])
roll = [*map(int, input().split())]

d = [(0, 0), (0, 1), (0, -1), (-1, 0), (1, 0)]
dice = [0, 0, 0, 0, 0, 0]
for r in roll:
    nx, ny = x+d[r][0], y+d[r][1]
    if 0 <= nx < n and 0 <= ny < m:
        new_dice = [[],
                    [dice[2], dice[1], dice[5], dice[0], dice[4], dice[3]],
                    [dice[3], dice[1], dice[0], dice[5], dice[4], dice[2]],
                    [dice[1], dice[5], dice[2], dice[3], dice[0], dice[4]],
                    [dice[4], dice[0], dice[2], dice[3], dice[5], dice[1]]
                    ]
        dice = new_dice[r]

        if arr[nx][ny] != 0:
            dice[0] = arr[nx][ny]
            arr[nx][ny] = 0
        else:
            arr[nx][ny] = dice[0]

        print(dice[5])
        x, y = nx, ny