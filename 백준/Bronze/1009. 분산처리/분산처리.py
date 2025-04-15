t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    n = a%10
    remains = [n]
    while True:
        next_n = (remains[-1] * n) % 10
        if next_n not in remains:
            remains.append(next_n)
            continue
        else:
            break
    iteration = b % len(remains)
    if remains[iteration-1] == 0:
        print(10)
    else:
        print(remains[iteration-1])