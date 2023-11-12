import sys
input = sys.stdin.readline

n = int(input())
arr = []
for _ in range(n):
    k = int(input())
    if k:
        arr.append(k)
    else:
        arr.pop()

print(sum(arr))