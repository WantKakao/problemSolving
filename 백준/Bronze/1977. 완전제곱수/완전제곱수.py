arr = [i**2 for i in range(1, 101)]
a = int(input())
b = int(input())
m = 0
s = 0
for n in range(a, b+1):
    if n in arr:
        s += n
        if m == 0:
            m = n
if s == 0:
    print(-1)
else:
    print(s)
    print(m)