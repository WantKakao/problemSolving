r, c = map(int, input().split())

now = 1
right = 3
down = 2
ans = 0

for i in range(r):
    a, b = divmod(c, 4)
    ans += 14 * a
    for j in range(b-1):
        if i % 2 == 0:
            ans += now
            temp = now
            now = 7 - right
            right = temp
        else:
            ans += now
            temp = now
            now = right
            right = 7 - temp
    if b == 0:
        continue
    else:
        ans += now
        temp = now
        now = 7 - down
        down = temp
print(ans)