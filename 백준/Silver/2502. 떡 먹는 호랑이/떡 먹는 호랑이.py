d, k = map(int, input().split())
l = [(1, 0), (0, 1)]
for _ in range(d-2):
    t = (l[0][0]+l[1][0], l[0][1]+l[1][1])
    l.pop(0)
    l.append(t)
i = 1
while 1:
    a = l[1][0]*i
    n = k - a
    if n % l[1][1] == 0:
        b = l[1][1] * (n // l[1][1])
        break
    i += 1
print(i)
print(n // l[1][1])