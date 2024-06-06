n = int(input())
tang = list(map(int, input().split()))

cnt = [0 for _ in range(10)]
cnt_type = 0
s = 0
ans = -1
for i in range(n):
    if cnt[tang[i]] == 0:
        cnt_type += 1

        if cnt_type > 2:
            if i-s > ans:
                ans = i-s
            while cnt[tang[s]] > 1:
                cnt[tang[s]] -= 1
                s += 1
            cnt[tang[s]] -= 1
            s += 1
            cnt_type -= 1

    cnt[tang[i]] += 1

if n-s > ans:
    ans = n-s

print(ans)