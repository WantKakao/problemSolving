from itertools import permutations

day, minus = map(int, input().split())
kit = list(map(int, input().split()))

ans = 0
order = permutations(kit, day)

for o in order:
    muscle = 500
    is_loss = False

    for k in o:
        muscle += (k - minus)
        if muscle < 500:
            is_loss = True
            break

    if not is_loss:
        ans += 1

print(ans)