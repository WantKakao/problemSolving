import sys
input = sys.stdin.readline

n = int(input())
l = []
for _ in range(n):
    l.append(int(input()))
l.sort(reverse=True)
for i in l:
    print(i)