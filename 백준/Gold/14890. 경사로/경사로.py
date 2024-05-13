import sys
input = sys.stdin.readline

n, l = map(int, input().split())
road = []
for _ in range(n):
    road.append(list(map(int, input().split())))
reverse_road = [[0 for _ in range(n)] for _ in range(n)]
for i in range(n):
    for j in range(n):
        reverse_road[i][j] = road[j][i]
runway = [[False for _ in range(n)] for _ in range(n)]


def find_runway(i, j, road):
    global ans, possible
    if abs(road[i][j + 1] - road[i][j]) > 1:
        possible = False
        return

    elif road[i][j + 1] == road[i][j] + 1:
        if j >= l-1:
            if any(road[i][j - k] != road[i][j] or runway[i][j - k] for k in range(l)):
                possible = False
                return
            else:
                for k in range(l):
                    runway[i][j - k] = True
        else:
            possible = False
            return

    elif road[i][j + 1] == road[i][j] - 1:
        if j < n - l:
            if any(road[i][j+k+1] != road[i][j+1] for k in range(l)):
                possible = False
                return
            else:
                for k in range(l):
                    runway[i][j+k+1] = True
        else:
            possible = False
            return


ans = 0
for i in range(n):
    possible = True
    for j in range(n-1):
        find_runway(i, j, road)
    if possible:
        ans += 1

runway = [[False for _ in range(n)] for _ in range(n)]
for i in range(n):
    possible = True
    for j in range(n-1):
        find_runway(i, j, reverse_road)
    if possible:
        ans += 1

print(ans)