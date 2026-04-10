n = int(input())
l = list(map(int, input().split()))
s = sum(l)
s2 = 0
for i in l:
    s2 += (i*i)
print((s*s - s2) // 2)