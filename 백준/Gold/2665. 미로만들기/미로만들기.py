import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().rstrip())) for _ in range(n)]

INF = int(1e9)
cost = [[INF]*n for _ in range(n)]

def bfs():
    dq = deque()
    dq.append((0, 0))
    cost[0][0] = 0

    d = [(-1,0),(0,1),(1,0),(0,-1)]

    while dq:
        x, y = dq.popleft()

        for dx, dy in d:
            nx, ny = x+dx, y+dy
            if 0 <= nx < n and 0 <= ny < n:
                # 흰방
                if graph[nx][ny] == 1 and cost[nx][ny] > cost[x][y]:
                    cost[nx][ny] = cost[x][y]
                    dq.appendleft((nx, ny))
                # 검은방
                elif graph[nx][ny] == 0 and cost[nx][ny] > cost[x][y] + 1:
                    cost[nx][ny] = cost[x][y] + 1
                    dq.append((nx, ny))

bfs()
print(cost[n-1][n-1])
