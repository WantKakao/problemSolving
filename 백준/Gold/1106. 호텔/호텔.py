C, N = map(int, input().split())
bag = []
for _ in range(N):
    bag.append(list(map(int, input().split())))

ans = [1e9 for _ in range(C+100)]
ans[0] = 0
for i in range(C):
    for b in bag:
        ans[i+b[1]] = min(ans[i+b[1]], ans[i]+b[0])

print(min(ans[C:]))