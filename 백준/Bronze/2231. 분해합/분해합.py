import sys
input = sys.stdin.readline

n = int(input())
l = len(str(n))
m = max(1, n-(l*9))

for i in range(m, n+1):
    str_i = str(i)
    str_sum = 0
    for j in str_i:
        str_sum += int(j)
    if i + str_sum == n:
        print(i)
        break

if n == 1 or i == n:
    print(0)
