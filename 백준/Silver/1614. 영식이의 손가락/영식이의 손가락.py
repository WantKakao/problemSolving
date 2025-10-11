n = int(input())
m = int(input())

d, e = divmod(m, 2)
if n == 1:
    ans = (8 * m)
elif n == 2:
    ans = 1 + (d * 8) + (e * 6)
elif n == 3:
    ans = 2 + (d * 8) + (e * 4)
elif n == 4:
    ans = 3 + (d * 8) + (e * 2)
else:
    ans = 4 + (8 * m)
print(ans)