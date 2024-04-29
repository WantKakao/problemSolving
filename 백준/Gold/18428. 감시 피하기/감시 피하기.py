from itertools import combinations

n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(str, input().split())))


# 찾으면 1 못찾으면 0 반환
def find_student(x, y):
    d = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for t in range(4):
        dx, dy = x, y
        while True:
            nx = dx + d[t][0]
            ny = dy + d[t][1]
            if nx >= n or nx < 0 or ny >= n or ny < 0 or arr[nx][ny] == 'T' or arr[nx][ny] == 'O':
                break
            if arr[nx][ny] == 'S':
                return 1
            dx, dy = nx, ny
    return 0


# obj = 장애물 놓을 수 있는 위치들
obj = []
for i in range(n):
    for j in range(n):
        if arr[i][j] == 'X':
            obj.append((i, j))

# case = 3개의 장애물을 설치한 상황들
case = combinations(obj, 3)
ans = 'NO'
for c in case:
    find = False
    for x, y in c:
        arr[x][y] = 'O'

    for i in range(n):
        for j in range(n):
            if arr[i][j] == 'T':
                s = find_student(i, j)
                if s == 1:
                    find = True

    if not find:
        ans = 'YES'
        break

    for x, y in c:
        arr[x][y] = 'X'

print(ans)