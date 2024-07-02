n = int(input())
house = []
for _ in range(n):
    house.append(list(map(int, input().split())))

# 파의프의 머리와 상태를 체크
house_layer = [[[0 for _ in range(3)] for _ in range(n)] for _ in range(n)]
house_layer[0][1][0] = 1

for i in range(n):
    for j in range(n):
        if j+1 < n and house[i][j+1] == 0:
            house_layer[i][j+1][0] += house_layer[i][j][0] + house_layer[i][j][1]
        if i+1 < n and house[i+1][j] == 0:
            house_layer[i+1][j][2] += house_layer[i][j][1] + house_layer[i][j][2]
        if i+1 < n and j+1 < n and house[i+1][j] == house[i][j+1] == house[i+1][j+1] == 0:
            house_layer[i+1][j+1][1] += house_layer[i][j][0] + house_layer[i][j][1] + house_layer[i][j][2]

print(sum(house_layer[n-1][n-1]))