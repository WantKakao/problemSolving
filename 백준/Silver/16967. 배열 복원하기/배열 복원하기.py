import sys
input = sys.stdin.readline

x1, y1, x2, y2 = map(int, input().split())
sumArr = []
for _ in range(x1+x2):
    sumArr.append([*map(int, input().split())])

arr = [[0 for _ in range(y1)] for _ in range(x1)]
for i in range(x2):
    for j in range(y1):
        arr[i][j] = sumArr[i][j]
for j in range(y2):
    for i in range(x1):
        arr[i][j] = sumArr[i][j]
for i in range(x2, x1):
    for j in range(y2, y1):
        arr[i][j] = sumArr[i][j] - arr[i-x2][j-y2]

for i in range(x1):
    for j in range(y1):
        print(arr[i][j], end=' ')
    print()
    