import copy

n = int(input())
ans = ''
ans_list = [('', -1000000000)]
for _ in range(n):
    a, c, t = map(str, input().split())
    if a == 'type':
        ans += c
    else:
        for i in range(len(ans_list)):
            if ans_list[i][1] >= int(t) - int(c):
                ans = ans_list[i-1][0]
                break
    ans_list.append((copy.deepcopy(ans), int(t)))

print(ans)