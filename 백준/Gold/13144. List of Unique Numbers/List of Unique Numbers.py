n = int(input())
arr = list(map(int, input().split()))

i, j = 0, 0
ans = 0
temp = {idx: 0 for idx in range(100001)}
while j < n:
    if temp[arr[j]] == 1:
        while arr[i] != arr[j]:
            ans += j-i
            temp[arr[i]] = 0
            i += 1
        ans += j - i
        temp[arr[i]] = 0
        i += 1

    temp[arr[j]] = 1
    j += 1

while i < j:
    ans += j-i
    i += 1

print(ans)