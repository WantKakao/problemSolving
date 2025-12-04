n = int(input())
l = []
for _ in range(n):
    num, strike, ball = map(int, input().split())
    l.append((str(num), strike, ball))

ans = 0
for i in range(100, 1000):
    str_i = str(i)
    if str_i[0] == str_i[1] or str_i[0] == str_i[2] or str_i[1] == str_i[2] or '0' in str_i:
        continue
    flag = False
    for num, strike, ball in l:
        s, b = 0, 0
        for j in range(3):
            if num[j] == str_i[j]:
                s += 1
            if str_i[j] in num:
                b += 1
        b -= s
        if s != strike or b != ball:
            flag = True
            break
    if not flag:
        ans += 1
        
print(ans)