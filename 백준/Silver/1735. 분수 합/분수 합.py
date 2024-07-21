a, b = map(int, input().split())
a2, b2 = map(int, input().split())

n, m = a*b2 + a2*b,  b*b2


def gcd(x, y):
    if x == 0:
        return y
    if y == 0:
        return x
    if x >= y:
        x %= y
    else:
        y %= x
    return gcd(x, y)


while True:
    g = gcd(n, m)
    if gcd(n, m) == 1:
        break
    n //= g
    m //= g

print(n, m)