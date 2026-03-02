n, m = map(int, input().split())
l = list(map(int, input().split()))
l.sort()
print(l[m-1])