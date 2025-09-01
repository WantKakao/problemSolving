from collections import Counter

n = int(input())
for _ in range(n):
    temp = list(map(int, input().split()))
    t, army = temp[0], temp[1:]
    counter = Counter(army)
    num, cnt = counter.most_common(1)[0]
    if cnt >= (t//2+1):
        print(num)
    else:
        print("SYJKGW")