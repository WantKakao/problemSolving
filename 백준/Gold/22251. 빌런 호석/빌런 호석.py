top, digit, total, n = map(int, input().split())

num = [[1, 1, 1, 0, 1, 1, 1],
       [0, 0, 1, 0, 0, 1, 0],
       [1, 0, 1, 1, 1, 0, 1],
       [1, 0, 1, 1, 0, 1, 1],
       [0, 1, 1, 1, 0, 1, 0],
       [1, 1, 0, 1, 0, 1, 1],
       [1, 1, 0, 1, 1, 1, 1],
       [1, 0, 1, 0, 0, 1, 0],
       [1, 1, 1, 1, 1, 1, 1],
       [1, 1, 1, 1, 0, 1, 1]]

no = str(n)
if len(no) < digit:
    now = (digit - len(no)) * '0' + no
else:
    now = no

ans = 0
arr = [[] for _ in range(digit)]
for i in range(digit):
    for j in range(10):
        temp = 0
        for k in range(7):
            if num[j][k] != num[int(now[i])][k]:
                temp += 1
        arr[i].append(temp)

for i in range(1, top+1):
    temp = 0
    floor = ('0' * (digit - len(str(i)))) + str(i)
    for j in range(digit):
        temp += arr[j][int(floor[j])]
    if temp <= total:
        ans += 1

print(ans-1)