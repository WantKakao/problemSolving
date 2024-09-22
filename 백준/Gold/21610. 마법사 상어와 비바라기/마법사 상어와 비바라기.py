import sys
input = sys.stdin.readline

N, M = map(int, input().split())
graph = []
for _ in range(N):
    graph.append([*map(int, input().split())])

moving = []
for _ in range(M):
    direction, movement = map(int, input().split())
    moving.append((direction, movement))

dx = [(0, 0), (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)]

# 처음에 구름의 위치를 set으로 변경
cloud = set([(N-2, 0), (N-2, 1), (N-1, 0), (N-1, 1)])

for idx in range(M):
    # 구름 이동
    new_cloud = set()
    for x, y in cloud:
        nx = (x + dx[moving[idx][0]][0] * moving[idx][1]) % N
        ny = (y + dx[moving[idx][0]][1] * moving[idx][1]) % N
        new_cloud.add((nx, ny))
    cloud = new_cloud

    # 물 증가
    for x, y in cloud:
        graph[x][y] += 1

    # 구름이 있는 위치에서 대각선 방향 물 복사
    for x, y in cloud:
        for k in [2, 4, 6, 8]:
            nx = x + dx[k][0]
            ny = y + dx[k][1]
            if 0 <= nx < N and 0 <= ny < N and graph[nx][ny]:
                graph[x][y] += 1

    # 새로운 구름 생성
    new_cloud = set()
    for i in range(N):
        for j in range(N):
            if graph[i][j] >= 2 and (i, j) not in cloud:
                new_cloud.add((i, j))
                graph[i][j] -= 2
    cloud = new_cloud

# 결과 출력
S = 0
for i in range(N):
    S += sum(graph[i])
print(S)
