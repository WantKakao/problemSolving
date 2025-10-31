n = input()
l = len(n)
ans = 0
for i in range(1, l):
    t = (10**i)-1
    b = 10**(i-1)
    ans += (t-b+1)*i
    ans %= 1234567
t = int(n)
b = 10**(l-1)
ans += (t-b+1)*l
ans %= 1234567
print(ans)