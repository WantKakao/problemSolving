import math

n, m = map(int, input().split())
nums = []
for _ in range(n):
     nums.append(list(input()))

def check_and_answer(number):
    global ans
    r = math.isqrt(int(number))
    if r**2 == int(number):
        ans = max(ans, int(number))

ans = -1
for i in range(n):
    for j in range(m):
        for ki in range(-9, 9):
            for kj in range(-9, 9):
                num, num2 = nums[i][j], nums[i][j]
                if ki==kj==0:
                    check_and_answer(int(num))
                    continue
                else:
                    ni, nj = i+ki, j+kj
                    while 0 <= ni < n and 0 <= nj < m:
                        num += nums[ni][nj]
                        check_and_answer(int(num))
                        ni, nj = ni+ki, nj+kj

print(ans)