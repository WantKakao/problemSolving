n = int(input())
move = list(map(str, input()))

x, y = 0, 0
maze = [(0, 0)]
dx = [(1, 0), (0, -1), (-1, 0), (0, 1)]
t = 0
for m in move:
    if m == 'F':
        x = x + dx[t][0]
        y = y + dx[t][1]
        maze.append((x, y))
    elif m == 'R':
        t = (t+1) % 4
    else:
        t = (t-1) % 4

min_x, min_y, max_x, max_y = 0, 0, 0, 0
for i, j in maze:
    if i < min_x:
        min_x = i
    elif i > max_x:
        max_x = i

    if j < min_y:
        min_y = j
    elif j > max_y:
        max_y = j

arr = [['#' for _ in range(min_y, max_y+1)] for _ in range(min_x, max_x+1)]
for i, j in maze:
    arr[i-min_x][j-min_y] = '.'

for i in range(len(arr)):
    print(''.join(arr[i]))