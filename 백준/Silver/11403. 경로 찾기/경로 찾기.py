import sys
input = sys.stdin.readline

n = int(input())
arr = []
for _ in range(n):
    arr.append([*map(int, input().split())])

for i in range(n):
    for j in range(n):
        if arr[i][j] == 0:
            arr[i][j] = 10000

for k in range(n):
    for i in range(n):
        for j in range(n):
            arr[i][j] = min(arr[i][j], arr[i][k]+arr[k][j])

for i in range(n):
    for j in range(n):
        if arr[i][j] == 10000:
            print(0, end=' ')
        else:
            print(1, end=' ')
    print()