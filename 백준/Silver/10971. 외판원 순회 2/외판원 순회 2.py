import sys
input = sys.stdin.readline

city = int(input())
road_map = []
visited = [False] * city
maximum = 10000000

for _ in range(city):
    road_map.append(list(map(int, input().split())))


def circuit(i, depth, cost):
    global maximum
    if depth == city-1:
        if cost+road_map[i][0] < maximum and road_map[i][0] != 0:
            maximum = cost+road_map[i][0]
        return
    for j in range(1, city):
        if road_map[i][j] != 0 and visited[j] == False:
            visited[i] = True
            circuit(j, depth+1, cost+road_map[i][j])
            visited[i] = False
    return

circuit(0, 0, 0)
print(maximum)