from collections import deque
import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    x1, y1 = map(int, input().split())
    x2, y2 = map(int, input().split())
    q = deque()
    q.append((x1, y1, 0))
    d = [(-2,-1),(-2,1),(-1,-2),(-1,2),(1,-2),(1,2),(2,-1),(2,1)]
    visited = [[0 for _ in range(n)] for _ in range(n)]
    while q:
        x, y, c = q.popleft()
        visited[x][y] = 1
        if x == x2 and y == y2:
            print(c)
            break
        for i in range(8):
            dx = x + d[i][0]
            dy = y + d[i][1]
            if 0 <= dx < n and 0 <= dy < n and visited[dx][dy] == 0:
                visited[dx][dy] = 1
                q.append((dx, dy, c+1))