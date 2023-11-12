from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append([*map(int, input().rstrip())])

d = [(0, 1), (0, -1), (1, 0), (-1, 0)]
q = deque()
q.append((0, 0, 1, 1))
visited = [[-1 for _ in range(m)] for _ in range(n)]
# cnt 를 바깥에서 설정하면 안됨
# 똑같은곳이라도 cnt = 1 로 돌아서올 수 있음


def bfs(flag):
    visited[0][0] = 1
    while q:
        x, y, cost, cnt = q.popleft()
        if x == n-1 and y == m-1:
            print(cost)
            flag = 1
            break
        for i in range(4):
            dx = x + d[i][0]
            dy = y + d[i][1]
            if 0 <= dx and dx < n and 0 <= dy and dy < m:
                if visited[dx][dy] < cnt and graph[dx][dy] == 0:
                    q.append((dx, dy, cost+1, cnt))
                    visited[dx][dy] = cnt
                elif visited[dx][dy] < cnt and graph[dx][dy] == 1 and cnt == 1:
                    q.append((dx, dy, cost+1, cnt-1))
                    visited[dx][dy] = cnt
    if not flag:
        print(-1)


bfs(0)