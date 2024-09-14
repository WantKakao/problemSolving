n = int(input())

order = []
for _ in range(n**2):
    p, f1, f2, f3, f4 = map(int, input().split())
    order.append((p, (f1, f2, f3, f4)))

graph = [[0 for _ in range(n)] for _ in range(n)]
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

for k in range(n**2):
    standard = -1
    idx = [0, 0]
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 0:
                temp = 0
                for t in range(4):
                    nx = i + dx[t]
                    ny = j + dy[t]
                    if 0 <= nx < n and 0 <= ny < n:
                        if graph[nx][ny] in order[k][1]:
                            temp += 10
                        if graph[nx][ny] == 0:
                            temp += 1
                if temp > standard:
                    standard = temp
                    idx = [i, j]
    graph[idx[0]][idx[1]] = order[k][0]

score = 0
for i in range(n):
    for j in range(n):
        for k in range(n**2):
            if order[k][0] == graph[i][j]:
                idx = k
        temp = 0
        for t in range(4):
            nx = i + dx[t]
            ny = j + dy[t]
            if 0 <= nx < n and 0 <= ny < n:
                if graph[nx][ny] in order[idx][1]:
                    temp += 1
        if temp == 4:
            score += 1000
        elif temp == 3:
            score += 100
        elif temp == 2:
            score += 10
        elif temp == 1:
            score += 1

print(score)