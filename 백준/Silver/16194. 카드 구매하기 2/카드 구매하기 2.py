n = int(input())
l = [0] + list(map(int, input().split()))
for i in range(1, n+1):
    for j in range(1, i):
        l[i] = min(l[i], l[i-j]+l[j])
print(l[n])