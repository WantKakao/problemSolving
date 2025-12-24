n = int(input())
l = list(map(int, input().split()))
s = set(l)
print(n-len(s))