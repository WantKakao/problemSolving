import math
l = int(input())
a = int(input())
b = int(input())
c = int(input())
d = int(input())
k1 = math.ceil(a/c)
k2 = math.ceil(b/d)
print(min(l-k1, l-k2))