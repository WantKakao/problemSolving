n = int(input())
for i in range(n):
    a = n-i-1
    s = ' '*a
    s += '*'*(2*i+1)
    print(s)
for i in range(n-2, -1, -1):
    a = n-i-1
    s = ' '*a
    s += '*'*(2*i+1)
    print(s)