import sys
import heapq
from collections import deque
input = sys.stdin.readline
idx = 1
while 1:
    n = int(input())
    if n == 0:
        break
    else:
        cave = []
        for _ in range(n):
            cave.append([*map(int, input().split())])
        cost = [[1e6 for _ in range(n)] for _ in range(n)]
        cost[0][0] = cave[0][0]
        # q = deque()
        q = [(0, 0, cave[0][0])]
        # q.append((0, 0, cave[0][0]))
        dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
        while q:
            # x, y, c = q.popleft()
            x, y, c = heapq.heappop(q)
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx < n and 0 <= ny < n:
                    temp = c + cave[nx][ny]
                    if temp < cost[nx][ny]:
                        # q.append((nx, ny, temp))
                        heapq.heappush(q, (nx, ny, temp))
                        cost[nx][ny] = temp
        print(f'Problem {idx}: {cost[-1][-1]}')
        idx += 1