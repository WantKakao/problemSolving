n = int(input())
board = [[0 for _ in range(n)] for _ in range(n)]
possibility = 0

def nQueen(row):
    global possibility
    if row == n:
        possibility += 1
        return

    for col in range(n):
        if board[row][col] == 0:
            board[row][col] += 1
            for i in range(row+1, n):
                board[i][col] += 1
                right = col+i-row
                left = col - i + row
                if right < n:
                    board[i][right] += 1
                if left >= 0:
                    board[i][left] += 1

            nQueen(row+1)

            board[row][col] -= 1
            for i in range(row + 1, n):
                board[i][col] -= 1
                right = col + i - row
                left = col - i + row
                if right < n:
                    board[i][right] -= 1
                if left >= 0:
                    board[i][left] -= 1
    return

nQueen(0)
print(possibility)