n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
    
a.sort()
ans = 5
for i in range(n):
    s = 0
    for t in range(a[i], a[i] + 5):
        if t in a:
            s += 1
    ans = min(5-s, ans)
    
print(ans)