t = int(input())
for _ in range(t):
    n, s = map(int, input().split())
    seats = [0 for _ in range(s)]
    for _ in range(n):
        ss = int(input())
        seats[ss-1] = 1
    print(n-sum(seats))