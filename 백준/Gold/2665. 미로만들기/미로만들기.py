import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
graph = []
for _ in range(n):
    graph.append([*map(int, input().rstrip())])
INF = 10e9
cost = [[INF for _ in range(n)] for _ in range(n)]

# print(graph)
q = deque()
def bfs():
    d = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    q.append((0, 0, 0)) # 시작점 (0, 0) 바꾼횟수 0
    while q:
        x, y, c = q.popleft()

        for i in range(4):
            new_x = x + d[i][0]
            new_y = y + d[i][1]
            if new_x >= 0 and new_y >= 0 and new_x < n and new_y < n:
                if graph[new_x][new_y] == 1 and cost[new_x][new_y] > c:    # 흰방 이면서 비용이 적을 때
                    q.append((new_x, new_y, c))
                    cost[new_x][new_y] = c
                elif graph[new_x][new_y] == 0 and cost[new_x][new_y] > c:   # 검은방 이면서 비용이 적을 때
                    q.append((new_x, new_y, c+1))
                    cost[new_x][new_y] = c+1
                else:
                    continue


bfs()

print(cost[n-1][n-1])