a, b, c, d = map(str, input().split())
n1 = int(a+b+c+d)
n2 = int(b+c+d+a)
n3 = int(c+d+a+b)
n4 = int(d+a+b+c)
n = min(n1, n2, n3, n4)
s = set()
for i in range(1111, 10000):
    w = str(i//1000)
    x = str((i//100)%10)
    y = str((i//10)%10)
    z = str(i%10)
    if w == '0' or x == '0' or y == '0' or z == '0':
        continue
    m1 = int(w+x+y+z)
    m2 = int(x+y+z+w)
    m3 = int(y+z+w+x)
    m4 = int(z+w+x+y)
    s.add(min(m1, m2, m3, m4))
ans = list(s)
ans.sort()
print(ans.index(n)+1)