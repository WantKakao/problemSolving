N, L = map(int, input().split())
loc = list(map(int, input().split()))
loc.sort()

tape = 0
ans = 0
for l in loc:
    if l <= tape:
        continue
    else:
        tape = l + L - 1
        ans += 1

print(ans)