n = int(input())
for i in range(n):
    s = ' '*(n-i-1)
    k = '*'*(i+1)
    sk = s+k
    print(sk)
for j in range(n-1):
    s = ' '*(j+1)
    k = '*'*(n-j-1)
    sk = s+k
    print(sk)