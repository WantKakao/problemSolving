n, k = map(int, input().split())
l = list(map(int, input().split()))

for i in range(k):
    l[i] = (l[i] // 2) + (l[i] % 2)
if n <= sum(l):
    print("YES")
else:
    print("NO")