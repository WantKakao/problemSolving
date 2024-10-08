arr = ['a', 'i', 'o', 'u', 'e']
ans = 0
s = input()
for i in s:
    if i in arr:
        ans += 1
print(ans)