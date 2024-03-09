import sys
input = sys.stdin.readline

n = int(input())
k = int(input())
sensor = [*map(int, input().split())]
sensor.sort()

distance = []
for i in range(1, n):
    dst = sensor[i] - sensor[i-1]
    distance.append(dst)

# print(sensor)
# print(distance)

distance.sort(reverse=True)
answer = distance[k-1:]
print(sum(answer))