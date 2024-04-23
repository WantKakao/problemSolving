import sys
input = sys.stdin.readline

n, m = map(int, input().split())
score_board = []
for _ in range(n):
    score_board.append([*map(int, input().split())])

block = [
    [(0, 1), (0, 2), (0, 3)], [(1, 0), (2, 0), (3, 0)], [(0, 1), (1, 0), (1, 1)],
    [(1, 0), (2, 0), (2, 1)], [(1, 0), (1, -1), (1, -2)], [(0, 1), (1, 1), (2, 1)], [(0, 1), (0, 2), (1, 0)],
    [(1, 0), (2, 0), (2, -1)], [(1, 0), (1, 1), (1, 2)], [(0, 1), (1, 0), (2, 0)], [(0, 1), (0, 2), (1, 2)],
    [(1, 0), (1, 1), (2, 1)], [(0, 1), (1, 0), (1, -1)], [(1, 0), (1, -1), (2, -1)], [(0, 1), (1, 1), (1, 2)],
    [(0, 1), (0, 2), (1, 1)], [(1, 0), (2, 0), (1, 1)], [(1, 0), (1, -1), (1, 1)], [(1, 0), (2, 0), (1, -1)],
    ]

ans = 0
for i in range(n):
    for j in range(m):
        for b in block:
            block_sum = score_board[i][j]
            for k in range(3):
                ni = i + b[k][0]
                nj = j + b[k][1]
                if ni < 0 or ni >= n or nj < 0 or nj >= m:
                    break
                block_sum += score_board[ni][nj]
                if block_sum > ans:
                    ans = block_sum

print(ans)