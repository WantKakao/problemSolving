n = int(input())
l = []
for _ in range(n):
    l.append(int(input()))
    
a = l[1] - l[0]
b = int(l[1] / l[0])
A = True
for i in range(2, n):
    if l[i] - l[i-1] != a:
        A = False
        
if A:
    print(l[-1] + a)
else:
    print(l[-1] * b)