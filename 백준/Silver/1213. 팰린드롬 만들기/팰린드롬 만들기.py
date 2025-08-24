S = input()
temp = []
odd = []
for s in S:
    if s in odd:
        odd.remove(s)
        temp.append(s)
    else:
        odd.append(s)

if len(odd) > 1:
    print("I'm Sorry Hansoo")
else:
    temp.sort()
    ans = []
    for t in temp:
        ans.append(t)
    for o in odd:
        ans.append(o)
    for t in reversed(temp):
        ans.append(t)
    for a in ans:
        print(a, end='')