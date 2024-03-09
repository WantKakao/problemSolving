n, m = map(int, input().split())
truth = list(map(int, input().split()))
people = truth[1:]
ans = 0
company = [[100 for _ in range(n+1)] for _ in range(n+1)]
allParty = []
for _ in range(m):
    party = list(map(int, input().split()))
    member = party[1:]
    allParty.append(member)
    for p in member:
        for i in member:
            company[p][i] = 1
            company[i][p] = 1

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            company[i][j] = min(company[i][j], company[i][k] + company[k][j])
lier = set(i for i in range(1, n+1))

for p in people:
    for i in range(1, n+1):
        if company[p][i] != 100:
            if i in lier:
                lier.remove(i)

for prt in allParty:
    tmp = 0
    for person in prt:
        if person not in lier:
            tmp = 1
            break
    if not tmp:
        ans += 1
print(ans)
