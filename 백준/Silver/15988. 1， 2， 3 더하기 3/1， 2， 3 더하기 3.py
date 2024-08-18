import sys
input = sys.stdin.readline

MOD = 1000000009

t = int(input())
for _ in range(t):
    n = int(input())
    
    if n == 1:
        print(1)
    elif n == 2:
        print(2)
    elif n == 3:
        print(4)
    else:
        a, b, c = 1, 2, 4
        for _ in range(n - 3):
            a, b, c = b, c, (a + b + c) % MOD
        print(c)
