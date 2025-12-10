n = int(input())
f = int(input())
d = n % f
n_2 = int(str(n)[-2:])
n_2 += (f-d)
while n_2 >= 0:
    n_2 -= f
ans = str(n_2+f)
if len(ans) == 1:
    print('0'+ans)
else:
    print(ans)