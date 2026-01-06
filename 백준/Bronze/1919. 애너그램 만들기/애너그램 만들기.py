from collections import Counter

a = input().rstrip()
b = input().rstrip()

ca = Counter(a)
cb = Counter(b)

ans = 0
for c in set(ca.keys()) | set(cb.keys()):
    ans += abs(ca[c] - cb[c])

print(ans)
