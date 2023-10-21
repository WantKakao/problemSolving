import sys
input = sys.stdin.readline
from collections import deque

x, y = map(int, input().split())
graph = []
q = deque()
for _ in range(x):
    graph.append([*map(int, input().rstrip())])
d = [(-1,0), (0,1), (1,0), (0,-1)]

# print(graph)
def bfs():
    q.append((0, 0, 2))
    while q:
        i, j, c = q.popleft()
        # print(q)
        # print(graph)
        for k in range(4):
            new_i = i + d[k][0]
            new_j = j + d[k][1]
            if new_i >= 0 and new_j >= 0 and new_i < x and new_j < y and graph[new_i][new_j] == 1:
                q.append((new_i, new_j, c+1))
                graph[new_i][new_j] = c

bfs()
# print(graph)
print(graph[x-1][y-1])