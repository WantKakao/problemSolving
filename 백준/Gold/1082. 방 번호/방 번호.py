n = int(input())
nums = list(map(int, input().split()))
m = int(input())

budget = ['0' for _ in range(m+1)]
for b in range(m):
    for i in range(n):
        if b+nums[i] <= m:
            budget[b+nums[i]] = str(max(int(budget[b+nums[i]]), int(budget[b]+str(i))))
            
print(int(budget[m]))