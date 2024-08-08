n = int(input())
l = list(map(int, input().split()))
s = set(l)
l = list(s)
l.sort()
for i in l:
    print(i, end=' ')