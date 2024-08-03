l = []
for _ in range(5):
    k = int(input())
    if k >= 40:
        l.append(k)
    else:
        l.append(40)
print(sum(l)//5)