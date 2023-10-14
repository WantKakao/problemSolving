def hanoi(n, start, end, inter):
    if n == 1:
        print(start, end)
    else:
        return hanoi(n - 1, start, inter, end), hanoi(1, start, end, inter), hanoi(n - 1, inter, end, start)


n = int(input())
count = [1 for _ in range(100)]
for i in range(99):
    count[i + 1] = 2 * count[i] + 1

print(count[n - 1])
if n <= 20:
    hanoi(n, 1, 3, 2)