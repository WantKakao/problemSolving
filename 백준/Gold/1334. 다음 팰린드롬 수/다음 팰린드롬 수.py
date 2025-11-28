import sys
num = int(input()) + 1
str_num = str(num)

if num < 10:
    print(num)
    sys.exit()

h = len(str_num) // 2
if len(str_num) % 2 == 0: # 짝수
    p = str_num[:h] + str_num[h-1::-1]
else: # 홀수
    p = str_num[:h+1] + str_num[h-1::-1]

if int(p) >= num:
    ans = int(p)
else:
    str_num = str(num + 10**h)
    if len(str_num) % 2 == 0: # 짝수
        p = str_num[:h] + str_num[h-1::-1]
    else: # 홀수
        p = str_num[:h+1] + str_num[h-1::-1]
    ans = int(p)
print(ans)