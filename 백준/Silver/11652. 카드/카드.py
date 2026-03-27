import sys
input = sys.stdin.readline

n = int(input())
d = dict()
for _ in range(n):
    k = int(input())
    if d.get(k):
        d[k] += 1
    else:
        d[k] = 1
        
a = 0
ans = 0
for key in d.keys():
    if d[key] > a or (d[key] == a and key < ans):
        ans = key
        a = d[key]
print(ans)
