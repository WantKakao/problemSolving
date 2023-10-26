from collections import deque

n, k = map(int, input().split())    # n = 크기 k = 바이러스 종류
area = [[]]                         # index 를 맞춰주기위해 빈배열 추가
for _ in range(n):
    area.append([0]+[*map(int, input().split())])   # 마찬가지로 index 0 일때 값 0 추가
s, ans_x, ans_y = map(int, input().split()) # s 초 후 (ans_x, ans_y) 의 바이러스 종류

q = deque()
for virus in range(1, k+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if area[i][j] == virus:          # 낮은 바이러스부터 감염시켜주기위함
                q.append((i, j, virus, 0))

d = [(-1, 0), (1, 0), (0, -1), (0, 1)]
while q:
    x, y, v, t = q.popleft()
    if t >= s:
        break
    for i in range(4):
        new_x = x + d[i][0]
        new_y = y + d[i][1]
        if new_x > 0 and new_y > 0 and new_x <= n and new_y <= n and not area[new_x][new_y]:    # 다음 area == 0 일때
            area[new_x][new_y] = v
            q.append((new_x, new_y, v, t+1))

print(area[ans_x][ans_y])