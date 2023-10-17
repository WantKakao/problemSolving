import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
k = int(input())
arr2 = list(map(int, input().split()))


def b_search(n):
    left = 0
    right = len(arr) - 1
    while left <= right:
        c = (left + right) // 2
        if n == arr[c]:
            return 1
        elif n > arr[c]:
            left = c + 1
        else:
            right = c - 1
    return 0


arr.sort()
for i in arr2:
    print(b_search(i))