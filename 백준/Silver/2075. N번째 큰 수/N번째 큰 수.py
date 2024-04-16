import sys
input = sys.stdin.readline

n = int(input())
arr = []
for i in range(n):
    arr += [*map(int, input().split())]
    arr.sort(reverse=True)
    arr = arr[:i+1]

print(arr[-1])