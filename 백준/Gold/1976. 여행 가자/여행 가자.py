import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
arr = []
for _ in range(n):
    arr.append([*map(int, input().split())])
course = [*map(int, input().split())]

for i in range(n):
    for j in range(n):
        if i == j:
            arr[i][j] = 1
        elif arr[i][j] == 0:
            arr[i][j] = 10

for k in range(n):
    for i in range(n):
        for j in range(n):
            arr[i][j] = min(arr[i][j], arr[i][k]+arr[k][j])

flag = 0
for i in range(m-1):
    if arr[course[i]-1][course[i+1]-1] == 10:
        print("NO")
        flag = 1
        break

if not flag:
    print("YES")