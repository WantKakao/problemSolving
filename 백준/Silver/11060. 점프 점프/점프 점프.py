n = int(input())
jump = list(map(int, input().split()))

idx = 0
ans = 0
end = True
while idx < n-1:
    ans += 1
    J = jump[idx]
    temp = 0

    for j in range(1, J+1):
        if idx+j >= n-1:
            k = n-1
            temp = 1
            break
        t = j + jump[idx+j]
        if t > temp:
            temp = t
            k = idx+j

    if temp == 0:
        end = False
        break
    idx = k

if end:
    print(ans)
else:
    print(-1)