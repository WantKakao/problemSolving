t = 1
while True:
    n = int(input())
    if n == 0:
        break
        
    name = []
    for _ in range(n):
        name.append(input())
    count = [0 for _ in range(n)]
    for _ in range(2*n-1):
        a, b = map(str, input().split())
        count[int(a)-1] += 1
    idx = count.index(1)
    print(t, end=' ')
    print(name[idx])
    t += 1