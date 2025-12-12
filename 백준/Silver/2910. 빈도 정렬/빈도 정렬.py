from collections import defaultdict

n, c = map(int, input().split())
l = list(map(int, input().split()))
d = defaultdict(int)
for i in l:
    d[i] += 1

sorted_items = sorted(d.items(), key=lambda x: -x[1])

for key, val in sorted_items:
    for _ in range(val):
        print(key, end=' ')