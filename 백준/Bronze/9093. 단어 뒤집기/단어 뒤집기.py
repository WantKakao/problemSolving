t = int(input())
for _ in range(t):
    l = list(map(str, input().split()))
    for i in l:
        print(i[::-1], end=' ')