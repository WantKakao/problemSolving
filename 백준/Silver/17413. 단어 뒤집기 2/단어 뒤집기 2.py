S = input().rstrip()
t = ''
flag = 0
for s in S:
    if s == '<':
        print(t[::-1], end='')
        t = ''
        flag = 1
    elif s == '>':
        flag = 0
        print(s, end='')
        continue
    if flag:
        print(s, end='')
        continue
    if s == ' ':
        print(t[::-1], end='')
        print(' ', end='')
        t = ''
    else:
        t += s
print(t[::-1], end='')