import sys
input = sys.stdin.readline

n = int(input())
l = []
for _ in range(n):
    name, a, b, c = map(str, input().rstrip().split())
    a, b, c = int(a), int(b), int(c)
    l.append([-a, b, -c, name])
l.sort()
for i in l:
    print(i[3])