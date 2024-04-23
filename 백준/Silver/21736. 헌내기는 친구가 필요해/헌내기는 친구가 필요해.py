from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
campus = []
for _ in range(n):
    campus.append([*map(str, input().rstrip())])


def find_friend(x, y, ans):
    q = deque([(x, y)])
    di = [0, 0, -1, 1]
    dj = [-1, 1, 0, 0]

    while q:
        i, j = q.popleft()
        for t in range(4):
            ni = i + di[t]
            nj = j + dj[t]
            if 0 <= ni < n and 0 <= nj < m:
                if campus[ni][nj] == 'X':
                    continue
                elif campus[ni][nj] == 'P':
                    ans += 1
                q.append((ni, nj))
                campus[ni][nj] = 'X'

    return ans


for i in range(n):
    for j in range(m):
        if campus[i][j] == 'I':
            friend = find_friend(i, j, 0)

if not friend:
    print("TT")
else:
    print(friend)