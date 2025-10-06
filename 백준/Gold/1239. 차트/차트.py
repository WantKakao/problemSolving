from itertools import permutations

n = int(input())
dogs = list(map(int, input().split()))

ans = 0
for P in permutations(dogs, n):
    cum_sum = 0
    cut = []
    for p in P:
        cum_sum += p
        cut.append(cum_sum)
    temp = 0
    for c in cut:
        if c > 50:
            break
        if c+50 in cut:
            temp += 1
    if temp > ans:
        ans = temp
        
print(ans)