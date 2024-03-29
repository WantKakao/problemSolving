import sys
input = sys.stdin.readline
n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))
ans = [0] * 3
def dfs(x, y, n):
    num = arr[x][y]
    for i in range(n):
        for j in range(n):
            if arr[x+i][y+j] != num:
                return False
    return True
def sol(x, y, n):
    if dfs(x, y, n):
        ans[arr[x][y]+1] += 1
    else:
        for k in range(3):
            for l in range(3):
                sol(x + k * (n//3), y + l * (n//3), n//3)
    return
sol(0, 0, n)
for i in range(3):
    print(ans[i])