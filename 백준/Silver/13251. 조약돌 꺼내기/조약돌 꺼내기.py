from math import comb

m = int(input())
l = list(map(int, input().split()))
k = int(input())
s = sum(l)
P = 0
for i in l:
    p = comb(i, k) / comb(s, k)
    P += p
print(P)