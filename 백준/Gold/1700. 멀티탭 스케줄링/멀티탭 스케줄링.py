import sys
input = sys.stdin.readline
import copy

n, k = map(int, input().split())
appliances = [*map(int, input().split())]
# print(appliances)
ans = 0
using = []
for i in range(k):
    if appliances[i] in using:
        continue
    elif len(using) < n:
        using.append(appliances[i])
        continue
    else:
        temp = copy.deepcopy(using)
        for j in range(i+1, k):
            if len(temp) == 1:
                break
            if appliances[j] in temp:
                temp.remove(appliances[j])
        # print(temp)
        # print(using)
        using.remove(temp[0])
        using.append(appliances[i])
        ans += 1
print(ans)