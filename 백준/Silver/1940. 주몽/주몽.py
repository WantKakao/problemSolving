n = int(input())
m = int(input())
armor = list(map(int, input().split()))
armor.sort()
ans = 0
i, j = 0, n-1
while i < j:
    t = armor[i] + armor[j]
    if t < m:
        i += 1
    elif t > m:
        j -= 1
    else:
        ans += 1
        i += 1
        j -= 1
print(ans)