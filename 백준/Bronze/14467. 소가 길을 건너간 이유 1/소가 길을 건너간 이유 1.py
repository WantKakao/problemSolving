# 14467 소가 길을 건너간 이유 1
n = int(input())
ans = 0
cow_zero = [0 for _ in range(11)]
cow_one = [0 for _ in range(11)]
for _ in range(n):
    c, l = map(int, input().split())
    if l == 0:
        if cow_one[c] == 1:
            ans += 1
        cow_one[c] = 0
        cow_zero[c] = 1
    else:
        if cow_zero[c] == 1:
            ans += 1
        cow_one[c] = 1
        cow_zero[c] = 0

print(ans)