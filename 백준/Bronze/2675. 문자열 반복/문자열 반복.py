p = int(input())

for _ in range(p):
    test = list(input())
    ans = ''
    for i in range(2, len(test)):
        ans += test[i] * int(test[0])
    print(ans)