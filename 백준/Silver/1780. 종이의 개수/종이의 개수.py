import sys
input = sys.stdin.readline

n = int(input())
arr = []
for _ in range(n):
    arr.append([*map(int, input().split())])
cnt1 = cnt2 = cnt3 = 0


def check(x, y, size):
    if size < 1:
        return
    global cnt1, cnt2, cnt3
    temp = 0
    isZero = 1
    for i in range(x, x + size):
        for j in range(y, y + size):
            temp += arr[i][j]
            if arr[i][j] != 0:
                isZero = 0
    if temp == -(size ** 2):
        cnt1 += 1
    elif temp == size ** 2:
        cnt3 += 1
    elif temp == 0 and isZero:
        cnt2 += 1
    else:
        check(x, y, size // 3)
        check(x, y + size // 3, size // 3)
        check(x, y + 2 * (size // 3), size // 3)
        check(x + size // 3, y, size // 3)
        check(x + size // 3, y + size // 3, size // 3)
        check(x + size // 3, y + 2 * (size // 3), size // 3)
        check(x + 2 * (size // 3), y, size // 3)
        check(x + 2 * (size // 3), y + size // 3, size // 3)
        check(x + 2 * (size // 3), y + 2 * (size // 3), size // 3)


check(0, 0, n)
print(cnt1)
print(cnt2)
print(cnt3)