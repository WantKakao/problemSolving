import sys
input = sys.stdin.readline

subject, mileage = map(int, input().split())
mileage_for_subject = []
ans = 0

for _ in range(subject):
    apply, seat = map(int, input().split())
    m = [*map(int, input().split())]
    if seat > apply:
        if mileage > 0:
            mileage -= 1
            ans += 1
        continue
    m.sort(reverse=True)
    mileage_for_subject.append(m[seat-1])

mileage_for_subject.sort()
for s in mileage_for_subject:
    if mileage >= s:
        ans += 1
        mileage -= s

print(ans)