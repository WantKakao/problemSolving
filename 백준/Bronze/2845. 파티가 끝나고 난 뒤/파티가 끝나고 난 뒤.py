a, b = map(int, input().split())
l = list(map(int, input().split()))
c = a*b
for i in l:
    print(i-c, end=' ')