n = int(input())
arr = list(map(int, input().split()))
ans = 0
temp = 1
for a in arr:
    if a == 1:
        ans += temp
        temp += 1
    else:
        temp = 1
print(ans)