import sys
input = sys.stdin.readline

n = int(input())
checkpoint = []
for _ in range(n):
    checkpoint.append([*map(int, input().split())])

total_distance = 0
for i in range(1, n):
    total_distance += abs(checkpoint[i][0] - checkpoint[i-1][0]) + abs(checkpoint[i][1] - checkpoint[i-1][1])

shortcut = 0
for i in range(1, n-1):
    temp = abs(checkpoint[i][0] - checkpoint[i-1][0]) + abs(checkpoint[i][1] - checkpoint[i-1][1])
    temp += abs(checkpoint[i+1][0] - checkpoint[i][0]) + abs(checkpoint[i+1][1] - checkpoint[i][1])
    temp -= abs(checkpoint[i+1][0] - checkpoint[i-1][0]) + abs(checkpoint[i+1][1] - checkpoint[i-1][1])

    if temp > shortcut:
        shortcut = temp

print(total_distance - shortcut)