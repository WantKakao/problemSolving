n = int(input())
l = list(map(int, input().split()))
t1 = 0
t2 = 0
for i in l:
    a = i // 30
    b = i // 60
    t1 += (a+1)
    t2 += (b+1)
if t1*10 > t2*15:
    print('M', t2*15)
elif t1*10 < t2*15:
    print('Y', t1*10)
else:
    print('Y M', t1*10)