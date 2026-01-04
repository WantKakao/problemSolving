l = list(map(str, input().split()))
n = ['i', 'pa', 'te', 'ni', 'niti', 'a', 'ali', 'nego', 'no', 'ili']
ans = ''
for i in range(len(l)):
    if i != 0 and l[i] in n:
        continue
    ans += l[i][0].upper()
print(ans)