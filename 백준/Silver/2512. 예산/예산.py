n = int(input())
arr = list(map(int, input().split()))
budget = int(input())


def total(money, array):
    t = 0
    for a in array:
        t += min(a, money)
    return t


arr.sort()
if sum(arr) <= budget:
    print(arr[-1])
else:
    ans = 0
    s = 0
    e = 100000
    flag = 0

    while s < e:
        m = (s+e)//2
        b = total(m, arr)
        if b <= budget:
            s = m+1
            ans = m
        else:
            e = m

    print(ans)