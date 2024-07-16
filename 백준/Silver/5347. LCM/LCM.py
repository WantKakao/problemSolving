import sys
input = sys.stdin.readline


def GCD(x, y):
    if x == 0:
        return y
    if y == 0:
        return x
    if x >= y:
        x %= y
        return GCD(x, y)
    else:
        y %= x
        return GCD(x, y)


t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    print(a * b // GCD(a, b))