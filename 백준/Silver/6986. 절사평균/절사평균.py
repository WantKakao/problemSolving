import sys
from decimal import Decimal, ROUND_HALF_UP
input = sys.stdin.readline

n, k = map(int, input().split())
score = []
for _ in range(n):
    score.append(float(input()))

score.sort()
score = score[k:n-k]
s1 = str(sum(score) / (n-2*k))
s2 = str((sum(score) + score[0]*k + score[-1]*k) / n)
s1_rounded = Decimal(s1).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
s2_rounded = Decimal(s2).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
print(f"{s1_rounded:.2f}")
print(f"{s2_rounded:.2f}")