N, T = map(int, input().split())

ans = 1e9
for n in range(N):
    S, I, C = map(int, input().split())
    if S+(I*(C-1)) < T:
        continue
    for c in range(C):
        if S+(I*c) >= T and ans > S+(I*c)-T:
            ans = S+(I*c)-T
            break
ans = -1 if ans == 1e9 else ans
print(ans)