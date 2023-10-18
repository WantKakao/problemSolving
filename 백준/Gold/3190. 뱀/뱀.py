import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

n = int(input())
apple = int(input())
apples = []
for _ in range(apple):
    apples.append([*map(int, input().split())])
turn = int(input())
turns = []
for _ in range(turn):
    turns.append([*map(str, input().split())])

board = [[0 for _ in range(n+1)] for _ in range(n+1)]

for x, y in apples:
    board[x][y] = 1

direction = [[-1, 0], [0, -1], [1, 0], [0, 1]]
snake = [[1, 1]]
i = 3
time = 0

def move(snake):
    global i, time
    if turns and time == int(turns[0][0]):
        if turns[0][1] == 'L':
            i = (i+1) % 4
        else:
            i = (i-1) % 4
        turns.pop(0)
    time += 1

    new_x = snake[-1][0] + direction[i][0]
    new_y = snake[-1][1] + direction[i][1]

    if new_x <= 0 or new_x > n or new_y <= 0 or new_y > n:
        return
    elif [new_x, new_y] in snake:
        return
    else:
        snake.append([new_x, new_y])
        if board[new_x][new_y] == 1:
            board[new_x][new_y] = 0
        else:
            snake.pop(0)
    move(snake)


move(snake)
print(time)