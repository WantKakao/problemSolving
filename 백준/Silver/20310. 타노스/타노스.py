s = list(map(str, input()))
one = s.count('1')//2
zero = s.count('0')//2

l = len(s)
i = 0
while one > 0:
    if s[i] == '1':
        s.pop(i)
        one -= 1
    else:
        i += 1

l = len(s)
j = l-1
while zero > 0:
    if s[j] == '0':
        s.pop(j)
        zero -= 1
    j -= 1

print(''.join(s))