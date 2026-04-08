import sys
input = sys.stdin.readline

n = int(input())
v = list(map(int, input().split()))

cur = v[-1]

for i in range(n-2, -1, -1):
    cur = ((cur + v[i] - 1) // v[i]) * v[i]

print(cur)
