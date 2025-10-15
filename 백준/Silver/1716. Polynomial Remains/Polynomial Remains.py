while True:
    n, r = map(int, input().split())
    if n == r == -1:
        break

    coef = list(map(int, input().split()))
    for i in range(n, r-1, -1):
        if coef[i] != 0:
            coef[i-r] -= coef[i]
            coef[i] = 0

    if sum(coef[:r]) == 0:
        print(0)
    else:
        print(*coef[:r])