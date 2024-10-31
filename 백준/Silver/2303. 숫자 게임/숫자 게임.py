from itertools import permutations
import sys
input = sys.stdin.readline

n = int(input())
ans_idx = 0
ans = 0
for i in range(n):
    arr = list(map(int, input().split()))
    p = permutations(arr, 3)
    temp = 0
    for x in p:
        t = sum(x) % 10
        if t > temp:
            temp = t
    if temp >= ans:
        ans_idx = i + 1
        ans = temp
print(ans_idx)