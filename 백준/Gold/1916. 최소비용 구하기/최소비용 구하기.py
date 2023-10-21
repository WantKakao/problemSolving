import sys
input = sys.stdin.readline

v = int(input())
e = int(input())
bus = [[] for _ in range(v+1)]
for _ in range(e):
    i, j, c = map(int, input().split())
    bus[i].append((j, c))
start, finish = map(int, input().split())

INF = 10e9
distance = [INF for _ in range(v+1)]    # start 에서 출발하는 비용
distance[start] = 0
check = [False for _ in range(v+1)] # 이미 했던 도시인지 검사
check[start] = True

# print(bus)
for j, c in bus[start]:
    distance[j] = min(distance[j], c)

while True:
    # print(distance)
    min_index = 0
    minimum = INF
    for i in range(1, v+1):
        if distance[i] < minimum and check[i] == False:
            minimum = distance[i]
            min_index = i
    check[min_index] = True
    # print(min_index, bus[min_index])
    # print(check)
    if min_index == 0:
        break
    for j, c in bus[min_index]:
        distance[j] = min(distance[j], distance[min_index] + c)

print(distance[finish])