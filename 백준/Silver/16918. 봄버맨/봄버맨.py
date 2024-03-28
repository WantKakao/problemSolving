import sys
input = sys.stdin.readline

r, c, n = map(int, input().split())
arr1 = []
for _ in range(r):
    arr1.append([*map(str, input().rstrip())])

arr2 = [['O' for _ in range(c)] for _ in range(r)]
arr3 = [['O' for _ in range(c)] for _ in range(r)]
arr4 = [['O' for _ in range(c)] for _ in range(r)]
d = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def make(arr1, arr3):
    for i in range(r):
        for j in range(c):
            if arr1[i][j] == 'O':
                arr3[i][j] = '.'
                for k in range(4):
                    ni = i + d[k][0]
                    nj = j + d[k][1]
                    if 0 <= ni < r and 0 <= nj < c:
                        arr3[ni][nj] = '.'


def bomb(arr):
    for i in range(r):
        for j in range(c):
            print(arr[i][j], end='')
        print()


make(arr1, arr3)
make(arr3, arr4)
if n == 1:
    bomb(arr1)
elif n % 4 == 1:
    bomb(arr4)
elif n % 2 == 0:
    bomb(arr2)
else:
    bomb(arr3)
