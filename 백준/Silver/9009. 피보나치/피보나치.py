import sys
input = sys.stdin.readline

t = int(input())
l = []
for _ in range(t):
    n = int(input())
    fibo = [0, 1, 1]
    i = 0
    while fibo[-1] <= n:
        k = fibo[i+1] + fibo[i+2]
        fibo.append(k)
        i += 1
    ans = []
    for j in range(len(fibo)-2, 0, -1):
        if fibo[j] <= n:
            ans.append(fibo[j])
            n -= fibo[j]
        if n == 0:
            break
    for s in range(len(ans)):
        print(ans[len(ans)-1-s], end=' ')

    print()