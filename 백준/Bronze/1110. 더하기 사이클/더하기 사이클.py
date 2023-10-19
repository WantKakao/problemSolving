import sys
input = sys.stdin.readline

n = int(input())
if n < 10:
    origin = '0'+str(n)
else:
    origin = str(n)
i = 0

# print(origin)
while True:
    # print(origin)
    add = str(int(origin[0]) + int(origin[1]))
    if int(add) < 10:
        new = origin[1] + add[0]
    else:
        new = origin[1] + add[1]
    i += 1
    if n == int(new):
        break
    origin = new

print(i)