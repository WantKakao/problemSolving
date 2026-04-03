s1 = input().rstrip()
s2 = input().rstrip()

l1 = len(s1)
l2 = len(s2)
p1 = 100 // l1
p2 = 100 // l2

t1 = s1 * (p1+1)
t2 = s2 * (p2+1)
v1 = t1[:100]
v2 = t2[:100]
if v1 == v2:
    print(1)
else:
    print(0)