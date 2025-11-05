n = int(input())
l = list(map(int, input().split()))
s = int(input())

sorted_l = sorted(l, reverse=True)
ans = []
for i in range(n):
    for M in sorted_l:
        idx = l.index(M)
        if idx <= s:
            ans.append(M)
            s -= idx
            l.pop(idx)
            sorted_l = sorted(l, reverse=True)
            break

print(*ans)