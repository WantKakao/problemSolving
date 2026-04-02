n = int(input())
l = list(map(int, input().split()))
l.sort()
i = 0
t = 1
while i < n:
    if l[i] <= t:
        t += l[i]
        i += 1
    else:
        break
print(t)