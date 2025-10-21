n = int(input())
l = list(map(int, input().split()))
c = [0 for _ in range(51)]
for i in range(51):
    k = l.count(i)
    c[i] = k

for i in range(50, -1, -1):
    if c[i] == i:
        print(i)
        break
    if i == 0 and c[i] != i:
        print(-1)