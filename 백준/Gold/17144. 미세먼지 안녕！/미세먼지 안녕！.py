import sys
input = sys.stdin.readline

R, C, T = map(int, input().split())
graph = []
for _ in range(R):
    graph.append([*map(int, input().split())])
dx = [(-1, 0), (1, 0), (0, -1), (0, 1)]
cleaner = []
for idx in range(R):
    if graph[idx][0] == -1:
        cleaner.append(idx)


def spread_dust():
    new_graph = [[0 for _ in range(C)] for _ in range(R)]
    for i in range(R):
        for j in range(C):
            if graph[i][j] > 0:
                amount = graph[i][j] // 5
                for d in range(4):
                    nx = i + dx[d][0]
                    ny = j + dx[d][1]
                    if 0 <= nx < R and 0 <= ny < C and graph[nx][ny] != -1:
                        new_graph[nx][ny] += amount
                        graph[i][j] -= amount
            new_graph[i][j] += graph[i][j]
    new_graph[cleaner[0]][0] = -1
    new_graph[cleaner[1]][0] = -1
    return new_graph


def cleaning_machine(a, b, r, c):
    up = []
    for x in range(a-1, -1, -1):
        up.append((x, 0))
    for y in range(1, c):
        up.append((0, y))
    for x in range(1, a+1):
        up.append((x, c-1))
    for y in range(c-2, 0, -1):
        up.append((a, y))
    for i in range(1, len(up)):
        graph[up[i-1][0]][up[i-1][1]] = graph[up[i][0]][up[i][1]]
    graph[up[-1][0]][up[-1][1]] = 0

    down = []
    for x in range(b+1, r):
        down.append((x, 0))
    for y in range(1, c):
        down.append((r-1, y))
    for x in range(r-2, b-1, -1):
        down.append((x, c-1))
    for y in range(c-2, 0, -1):
        down.append((b, y))
    for i in range(1, len(down)):
        graph[down[i-1][0]][down[i-1][1]] = graph[down[i][0]][down[i][1]]
    graph[down[-1][0]][down[-1][1]] = 0


t = 0
while t < T:
    graph = spread_dust()
    cleaning_machine(cleaner[0], cleaner[1], R, C)
    t += 1

dust = 2
for idx in range(len(graph)):
    dust += sum(graph[idx])
print(dust)
