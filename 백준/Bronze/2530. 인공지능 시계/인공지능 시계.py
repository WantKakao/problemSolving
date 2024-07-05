h, m, s = map(int, input().split())
t = int(input())

h += t // 3600
t %= 3600
m += t // 60
t %= 60
s += t
if s >= 60:
    m += 1
    s -= 60
if m >= 60:
    h += 1
    m -= 60
if h >= 24:
    h %= 24
print(h, m, s)