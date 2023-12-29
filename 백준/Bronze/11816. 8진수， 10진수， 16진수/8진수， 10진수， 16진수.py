import sys
n = [*map(str, input())]
if n[0] == '0':
    if n[1] == 'x':
        k = 0
        m = 1
        for i in n[-1:1:-1]:
            if i == 'a':
                i = 10
            elif i == 'b':
                i = 11
            elif i == 'c':
                i = 12
            elif i == 'd':
                i = 13
            elif i == 'e':
                i = 14
            elif i == 'f':
                i = 15
            k += int(i) * m
            m *= 16
        print(k)
    else:
        k = 0
        m = 1
        for i in n[-1:0:-1]:
            k += int(i) * m
            m *= 8
        print(k)
else:
    k = ''
    for i in n:
        k += i
    print(int(k))