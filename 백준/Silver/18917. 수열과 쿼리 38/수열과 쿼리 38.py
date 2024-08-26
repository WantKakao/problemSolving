import sys

input = sys.stdin.readline

m = int(input())
counts = {}
sum_q = 0
xor_q = 0

for _ in range(m):
    k = input().rstrip()
    command = k[0]

    if command == '1':
        value = int(k[2:])
        if value in counts:
            xor_q ^= value
            counts[value] += 1
        else:
            counts[value] = 1
            xor_q ^= value
        sum_q += value
    elif command == '2':
        value = int(k[2:])
        xor_q ^= value
        counts[value] -= 1
        sum_q -= value
    elif command == '3':
        print(sum_q)
    elif command == '4':
        print(xor_q)
