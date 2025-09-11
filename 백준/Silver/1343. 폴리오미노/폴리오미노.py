S = input()
splitted_S = S.split('.')
is_possible = True
ans = ''
for s in splitted_S:
    l = len(s)
    while l >= 4:
        l -= 4
        ans += 'AAAA'
    if l >= 2:
        l -= 2
        ans += 'BB'
    if l == 1:
        is_possible = False
    if not is_possible:
        break
    ans += '.'

if is_possible:
    print(ans[:-1])
else:
    print(-1)