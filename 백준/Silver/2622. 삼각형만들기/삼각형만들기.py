import math
n = int(input())

end = (n-1)//2
start = math.ceil(n/3)
ans = 0
if n == 1 or n == 2 or n == 4:
    print(0)
else:
    for i in range(end, start-1, -1):
        j = i
        k = n - 2*i
        ans += (j - k)//2 + 1
    print(ans)
