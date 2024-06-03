import sys
input = sys.stdin.readline

king, stone, n = map(str, input().rstrip().split())
king_x = 8-int(king[1])
king_y = ord(king[0])-65
stone_x = 8-int(stone[1])
stone_y = ord(stone[0])-65

move = ['R', 'L', 'B', 'T', 'RT', 'LT', 'RB', 'LB']
dx = [(0, 1), (0, -1), (1, 0), (-1, 0), (-1, 1), (-1, -1), (1, 1), (1, -1)]

for _ in range(int(n)):
    m = input().rstrip()
    i = move.index(m)
    nx = king_x + dx[i][0]
    ny = king_y + dx[i][1]

    if 0 <= nx < 8 and 0 <= ny < 8:
        if nx == stone_x and ny == stone_y:
            s_nx = stone_x + dx[i][0]
            s_ny = stone_y + dx[i][1]
            if 0 <= s_nx < 8 and 0 <= s_ny < 8:
                stone_x = s_nx
                stone_y = s_ny
                king_x = nx
                king_y = ny
        else:
            king_x = nx
            king_y = ny

print(f"{chr(king_y+65)}{8-king_x}")
print(f"{chr(stone_y+65)}{8-stone_x}")