n = int(input())
l = list(map(int, input().split()))
l.sort()
if n % 2 == 1:
    print(l[n//2])
else:
    a, b = l[n//2-1], l[n//2]
    ans_a, ans_b = 0, 0
    for i in l:
        ans_a += abs(a-i)
        ans_b += abs(b-i)
    if ans_a <= ans_b:
        print(a)
    else:
        print(b)