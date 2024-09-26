n = int(input())
for _ in range(n):
    score = [*map(int, input().split())]
    score.sort()
    ans = score[1:4]
    if ans[2] - ans[0] > 3:
        print('KIN')
    else:
        print(sum(ans))