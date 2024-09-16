import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
fires = []
for _ in range(M):
    r, c, m, s, d = map(int, input().split())
    fires.append((r-1, c-1, m, s, d))
dx = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]

t = 0
while t < K:
    graph = [[[] for _ in range(N)] for _ in range(N)]
    temp_fires = []
    for r, c, m, s, d in fires:
        # 이동하기
        new_r = (r + dx[d][0] * s) % N
        new_c = (c + dx[d][1] * s) % N
        graph[new_r][new_c].append([m, s, d])

    for i in range(N):
        for j in range(N):
            if len(graph[i][j]) == 1:
                temp_fires.append((i, j, graph[i][j][0][0], graph[i][j][0][1], graph[i][j][0][2]))
            elif len(graph[i][j]) >= 2:
                sum_m, sum_s, sum_d = 0, 0, []
                for m, s, d in graph[i][j]:
                    sum_m += m
                    sum_s += s
                    sum_d.append(d % 2)
                new_m = sum_m // 5
                if new_m > 0:
                    new_s = sum_s // len(graph[i][j])
                    if 0 in sum_d and 1 in sum_d:
                        temp_fires.append((i, j, new_m, new_s, 1))
                        temp_fires.append((i, j, new_m, new_s, 3))
                        temp_fires.append((i, j, new_m, new_s, 5))
                        temp_fires.append((i, j, new_m, new_s, 7))
                    else:
                        temp_fires.append((i, j, new_m, new_s, 0))
                        temp_fires.append((i, j, new_m, new_s, 2))
                        temp_fires.append((i, j, new_m, new_s, 4))
                        temp_fires.append((i, j, new_m, new_s, 6))

    fires = temp_fires
    t += 1

if fires:
    ans = 0
    for f in fires:
        ans += f[2]
    print(ans)
else:
    print(0)