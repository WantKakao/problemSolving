import sys
input = sys.stdin.readline
from itertools import permutations

n = int(input())
nums = [*map(int, input().split())]
oper_nums = [*map(int, input().split())]
oper = []
for _ in range(oper_nums[0]):
    oper.append('+')
for _ in range(oper_nums[1]):
    oper.append('-')
for _ in range(oper_nums[2]):
    oper.append('*')
for _ in range(oper_nums[3]):
    oper.append('//')
# print(oper)
per = [*permutations(oper)]
per = set(per)

# print(per)
ans = []
for p in per:
    num = nums[0]
    for i in range(n-1):
        if p[i] == '+':
            num += nums[i+1]
        elif p[i] == '-':
            num -= nums[i+1]
        elif p[i] == '*':
            num *= nums[i+1]
        else:
            if num < 0:
                temp = -num // nums[i+1]
                num = -temp
            else:
                num //= nums[i+1]
    ans.append(num)
print(max(ans))
print(min(ans))