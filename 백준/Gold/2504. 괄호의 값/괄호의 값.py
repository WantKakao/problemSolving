import sys
input = sys.stdin.readline

brackets = list(input().strip())
# print(brackets)
a, b = 0, 0
d = []

for i in brackets:  # 올바른 괄호열

    if i == '(':
        a += 1
        d.append('(')

    elif i == '[':
        b += 1
        d.append('[')

    elif i == ')':
        a -= 1
        if a < 0:
            break
        else:
            if d[-1] == '(':    # 마지막 입력이 열린괄호 일시
                d.pop()
                if not d or d[-1] == '(' or d[-1] == '[':
                    d.append(2)
                else:   # 같은 선상에 숫자를 더함
                    tt = d.pop()
                    d.append(2 + tt)
            elif d[-1] == '[':
                break
            else:   # 마지막 입력이 숫자일시
                t = d.pop()
                d.pop()
                if not d or d[-1] == '(' or d[-1] == '[':
                    d.append(t*2)
                else:
                    tt = d.pop()
                    d.append(t*2 + tt)

    else:
        b -= 1
        if b < 0:
            break
        else:
            if d[-1] == '[':    # 마지막 입력이 열린괄호 일시
                d.pop()
                if not d or d[-1] == '(' or d[-1] == '[':
                    d.append(3)
                else:   # 같은 선상에 숫자를 더함
                    tt = d.pop()
                    d.append(3 + tt)
            elif d[-1] == '(':
                break
            else:   # 마지막 입력이 숫자일시
                t = d.pop()
                d.pop()
                if not d or d[-1] == '(' or d[-1] == '[':
                    d.append(t*3)
                else:
                    tt = d.pop()
                    d.append(t*3 + tt)


# print(a, b)
if a == b == 0 and d:
    # print(c)
    print(d[0])

else:
    print(0)