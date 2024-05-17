from itertools import combinations
import sys
input = sys.stdin.readline

n, survive = map(int, input().split())
city = []
for _ in range(n):
    city.append(list(map(int, input().split())))

house = []
chicken = []
for i in range(n):
    for j in range(n):
        if city[i][j] == 1:
            house.append((i, j))
        elif city[i][j] == 2:
            chicken.append((i, j))

case = combinations(chicken, survive)
answer = 1e9
for c in case:
    ans = 0
    for x, y in house:
        dist = 1e9
        for cx, cy in c:
            temp = abs(x-cx) + abs(y-cy)
            if temp < dist:
                dist = temp
        ans += dist
    if ans < answer:
        answer = ans

print(answer)