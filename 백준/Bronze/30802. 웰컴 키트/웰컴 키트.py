n = int(input())
shirt = [*map(int, input().split())]
T, P = map(int, input().split())

ans_t = 0
ans_p1, ans_p2 = 0, 0
for s in shirt:
    ans_t += s // T
    if s % T != 0:
        ans_t += 1
ans_p1, ans_p2 = divmod(n, P)
print(ans_t)
print(ans_p1, ans_p2)