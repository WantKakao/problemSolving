layout = input()

i = 1
l = len(layout)
stack = 0
ans = 0
while i < l:
    if layout[i] == '(':
        if layout[i-1] == '(':
            stack += 1
    else:
        if layout[i-1] == '(':
            ans += stack
        else:
            stack -= 1
            ans += 1
    i += 1

print(ans)