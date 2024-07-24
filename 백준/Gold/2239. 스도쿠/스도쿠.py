def print_board(board):
    for row in board:
        print("".join(row))


def is_valid(board, r, c, num):
    # Check if num is not in the current row
    if str(num) in board[r]:
        return False

    # Check if num is not in the current column
    for row in range(9):
        if board[row][c] == str(num):
            return False

    # Check if num is not in the 3x3 sub-grid
    start_row, start_col = 3 * (r // 3), 3 * (c // 3)
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if board[i][j] == str(num):
                return False

    return True


def solve_sudoku(board):
    # Find the next empty space
    for r in range(9):
        for c in range(9):
            if board[r][c] == '0':
                # Try every number from 1 to 9
                for num in range(1, 10):
                    if is_valid(board, r, c, num):
                        board[r][c] = str(num)
                        if solve_sudoku(board):
                            return True
                        board[r][c] = '0'
                return False
    return True


import sys
input = sys.stdin.readline

board = []
for _ in range(9):
    data = list(input().rstrip())
    board.append(data)

solve_sudoku(board)
print_board(board)
