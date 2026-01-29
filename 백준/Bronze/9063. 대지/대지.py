import sys
input = sys.stdin.readline

n = int(input().rstrip())
mx, my, Mx, My = 10000, 10000, -10000, -10000
for _ in range(n):
    x, y = map(int, input().rstrip().split())
    if x < mx:
        mx = x
    if y < my:
        my = y
    if x > Mx:
        Mx = x
    if y > My:
        My = y
print((Mx-mx)*(My-my))