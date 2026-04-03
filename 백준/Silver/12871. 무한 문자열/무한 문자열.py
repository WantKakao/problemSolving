import math

s1 = input().rstrip()
s2 = input().rstrip()

lcm = (len(s1) * len(s2)) // math.gcd(len(s1), len(s2))

if s1 * (lcm // len(s1)) == s2 * (lcm // len(s2)):
    print(1)
else:
    print(0)
