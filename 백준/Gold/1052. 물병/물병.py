n, k = map(int, input().split())
sqr = 0
ans = True
while 1:
    if 2**sqr > n:
        break
    elif 2**sqr < n:
        sqr += 1
    else:
        ans = False
        break
        
k -= 1
sqr -= 1
n -= 2**sqr

while k:
    sqr -= 1
    if n > 2**sqr:
        k -= 1
        n -= 2**sqr
    elif n == 2**sqr:
        ans = False
        break

if not ans:
    print(0)
else:
    print(2**sqr - n)