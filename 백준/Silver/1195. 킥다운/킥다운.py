a = list(input())
b = list(input())
    
L = max(len(a), len(b))
ans1, ans2 = len(a)+len(b), len(a)+len(b)
for i in range(len(a)):
    cnt = False
    for j in range(len(b)):
        if i+j < len(a) and a[i+j] == b[j] == '2':
            cnt = True
            break
    if not cnt:
        ans1 = max(L, i+len(b))
        break

for i in range(len(b)):
    cnt = False
    for j in range(len(a)):
        if i+j < len(b) and b[i+j] == a[j] == '2':
            cnt = True
            break
    if not cnt:
        ans2 = max(L, i+len(a))
        break

print(min(ans1, ans2))