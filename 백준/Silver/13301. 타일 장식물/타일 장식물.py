n = int(input())
l = [1, 1, 2]
for _ in range(n-1):
    t = l[1] + l[2]
    l.pop(0)
    l.append(t)
print(2*(l[0]+l[1]))