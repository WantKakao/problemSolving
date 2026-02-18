import sys
input = sys.stdin.readline

n = int(input())
d = dict()
d['ChongChong'] = 1
for _ in range(n):
    a, b = map(str, input().rstrip().split())
    if d.get(a) and not d.get(b):
        d[b] = 1
    if d.get(b) and not d.get(a):
        d[a] = 1
print(len(d))