# import sys
# input = sys.stdin.readline

n = int(input())
men = list(map(int, input().split()))
women = list(map(int, input().split()))

minus_men, plus_men, minus_women, plus_women = [], [], [], []
for i in range(n):
    if men[i] < 0:
        minus_men.append(men[i])
    else:
        plus_men.append(men[i])
    if women[i] < 0:
        minus_women.append(women[i])
    else:
        plus_women.append(women[i])

minus_men.sort()
plus_men.sort()
minus_women.sort()
plus_women.sort()

ans = 0
mm, pm, mw, pw = len(minus_men), len(plus_men), len(minus_women), len(plus_women)
i, j = 0, pw-1
while i < mm and j >= 0:
    if abs(minus_men[i]) > plus_women[j]:
        ans += 1
        i += 1
        j -= 1
    else:
        j -= 1

i, j = 0, pm-1
while i < mw and j >= 0:
    if abs(minus_women[i]) > plus_men[j]:
        ans += 1
        i += 1
        j -= 1
    else:
        j -= 1

print(ans)