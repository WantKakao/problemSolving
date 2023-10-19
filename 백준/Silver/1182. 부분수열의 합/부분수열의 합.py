import sys
input = sys.stdin.readline

n, s = map(int, input().split())
nums = [*map(int, input().split())]
ans = 0
# print(nums)
# combination (n < 20)
# n 개중 r 개를 뽑는 조합을 r=1 에서 r=len(nums) 까지 돌림

def combi(a, i, r, l, sum):
    global ans
    if r == a:
        if sum == s:
            ans += 1
        return
    else:
        for x in range(i, l):
            combi(a, x+1, r+1, l, sum+nums[x])
    return

l = len(nums)
for num in range(1, l+1):
    combi(num, 0, 0, l, 0)
print(ans)