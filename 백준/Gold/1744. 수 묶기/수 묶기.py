n = int(input())

ans = 0
pos_num = []
neg_num = []
zero = []
for _ in range(n):
    m = int(input())
    if m == 0:
        zero.append(m)
    elif m == 1:
        ans += 1
    elif m > 1:
        pos_num.append(m)
    else:
        neg_num.append(m)

pos_num.sort(reverse=True)
neg_num.sort()
while len(neg_num) >= 2:
    a = neg_num.pop(0)
    b = neg_num.pop(0)
    ans += a*b
if len(neg_num) == 1:
    if len(zero) == 0:
        ans += neg_num[0]

while len(pos_num) >= 2:
    a = pos_num.pop(0)
    b = pos_num.pop(0)
    ans += a*b
if len(pos_num) == 1:
    ans += pos_num[0]

print(ans)