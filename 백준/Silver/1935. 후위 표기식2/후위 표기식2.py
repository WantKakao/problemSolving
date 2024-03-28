import copy
import sys
input = sys.stdin.readline

n = int(input())
arr = [*map(str, input().rstrip())]
nums = []
arr2 = copy.deepcopy(arr)

for _ in range(n):
    nums.append(int(input()))
for i in range(n):
    for j in range(len(arr)):
        if ord(arr[j]) == 65 + i:
            arr2[j] = nums[i]

q = []
i = 0
for cmd in arr2:
    if cmd in ['+', '-', '*', '/']:
        a = q.pop()
        b = q.pop()
        if cmd == '+':
            q.append(b+a)
        elif cmd == '-':
            q.append(b-a)
        elif cmd == '*':
            q.append(b*a)
        else:
            q.append(b/a)
    else:
        q.append(cmd)

print(f'{q[0]:.2f}')
