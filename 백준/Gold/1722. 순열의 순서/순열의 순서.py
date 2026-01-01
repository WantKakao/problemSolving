n = int(input())
l = list(map(int, input().split()))
k = [i+1 for i in range(n)]

if l[0] == 1:
    new_k = []
    ans = 1
    for i in range(1, n+1):
        ans *= i
    for i in range(n):
        ans //= (n-i)
        if l[1] > ans:
            j = (l[1]-1)//ans
            new_k.append(k.pop(j))
            l[1] -= ((l[1]-1)//ans)*ans
        else:
            new_k.append(k.pop(0))
    print(' '.join(map(str, new_k)))
else:
    count = 1
    l = l[1:]
    ans = 1
    for i in range(1, n+1):
        ans *= i
    for i in range(n):
        ans //= (n-i)
        num = l.pop(0)
        if num != k[0]:
            count += (k.index(num) * ans)
            k.remove(num)
        else:
            k.pop(0)
    print(count)