import sys
input = sys.stdin.readline

N, M, L, K = map(int, input().split())
star = []
star_x, star_y = [], []
for _ in range(K):
    x, y = map(int, input().split())
    star.append((x, y))
    star_x.append(x)
    star_y.append(y)

answer = 0
for i in star_x:
    for j in star_y:

        star_count = 0
        for k in range(K):
            if i <= star_x[k] <= i+L and j <= star_y[k] <= j+L:
                star_count += 1

        if star_count > answer:
            answer = star_count

print(K-answer)