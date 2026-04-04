import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    l = list(map(int, input().split()))
    n2 = int(input())
    l2 = list(map(int, input().split()))
    d = dict()
    for i in l:
        d[i] = 1
    for j in l2:
        if d.get(j):
            print(1)
        else:
            print(0)