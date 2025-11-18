import math, sys
n = int(input())
s = int(math.sqrt(n))+1

if n <= 4:
    print(4)
    sys.exit()
    
ans = 1e9
for i in range(2, s+1):
    t, d = divmod(n, i)
    t = t+1 if d != 0 else t
    ans = min(ans, 2*(t+i-2))
print(ans)