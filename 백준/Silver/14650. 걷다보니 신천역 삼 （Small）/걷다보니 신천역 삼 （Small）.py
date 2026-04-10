n = int(input())
ans = 0
def three(s):
    global ans
    if len(s) == n:
        if int(s) % 3 == 0:
            ans += 1
        return
    for i in range(3):
        three(s+str(i))
    return
three('1')
three('2')
print(ans)