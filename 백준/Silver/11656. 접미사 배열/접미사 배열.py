s = input()
l = len(s)
L = []
for i in range(1, l+1):
    n = s[l-i:]
    L.append(n)
L.sort()
for j in L:
    print(j)