import sys
from collections import deque
input = sys.stdin.readline


def bfs(z, x, y):
    q = deque()
    q.append((z, x, y, 0))
    d = [(-1, 0, 0), (1, 0, 0), (0, -1, 0), (0, 1, 0), (0, 0, -1), (0, 0, 1)]

    while q:
        l, r, c, time = q.popleft()
        for t in range(6):
            nl, nr, nc = l + d[t][0], r + d[t][1], c + d[t][2]
            if 0 <= nl < L and 0 <= nr < R and 0 <= nc < C:
                if building[nl][nr][nc] == 'E':
                    return time + 1
                elif building[nl][nr][nc] == '.':
                    building[nl][nr][nc] = 'O'
                    q.append((nl, nr, nc, time + 1))

    return 0


while True:
    L, R, C = map(int, input().split())

    if L == R == C == 0:
        break

    # building = [층][행][열] = [L][R][C] = [k][i][j]
    building = [[] for _ in range(L)]
    for k in range(L):
        for i in range(R):
            building[k].append([*map(str, input().rstrip())])
        input()

    for k in range(L):
        for i in range(R):
            for j in range(C):
                if building[k][i][j] == 'S':
                    ans = bfs(k, i, j)

    if ans == 0:
        print("Trapped!")
    else:
        print(f"Escaped in {ans} minute(s).")
