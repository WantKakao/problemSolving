S = 0
nums = []
counts = []
for _ in range(10):
    n = int(input())
    S += n
    if n not in nums:
        nums.append(n)
        counts.append(1)
    else:
        idx = nums.index(n)
        counts[idx] += 1

c = counts.index(max(counts))        
print(S//10)
print(nums[c])
