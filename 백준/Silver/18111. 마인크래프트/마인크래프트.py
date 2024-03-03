import sys
input = sys.stdin.readline

n, m, b = map(int, input().split())
ground = []
for _ in range(n):
    ground.append([*map(int, input().split())])

ans = 1e9
height = 0
for h in range(257):
    up = 0
    down = 0
    tempAns = 0
    for i in range(n):
        for j in range(m):
            if h > ground[i][j]:
                up += h-ground[i][j]
            else:
                down += ground[i][j]-h
    if b+down >= up:
        tempAns = up + 2*down
        if tempAns <= ans:
            ans = tempAns
            height = h
    else:
        continue

print(ans, end=' ')
print(height)