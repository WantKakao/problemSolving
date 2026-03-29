n = int(input())
l = [0, 1, 1]
if n < 3:
    print(l[n])
else:
    for _ in range(n-2):
        t = (l[1] + l[2]) % 1000000007
        l.pop(0)
        l.append(t)    
    print(l[2])