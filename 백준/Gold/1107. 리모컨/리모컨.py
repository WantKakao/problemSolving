channel = input()
m = int(input())

ans1 = abs(100 - int(channel))

if m == 0:
    ans2 = len(channel)
    print(min(ans1, ans2))

elif m == 10:
    print(ans1)

else:
    error = list(map(int, input().split()))
    i = 0
    while True:
        channel_plus = str(int(channel) + i)
        channel_minus = str(int(channel) - i)
        if int(channel_minus) >= 0 and not any(int(c) in error for c in channel_minus):
            flag = True
            break
        if not any(int(c) in error for c in channel_plus):
            flag = False
            break
        i += 1

    if flag:
        ans2 = len(channel_minus) + i
    else:
        ans2 = len(channel_plus) + i
    print(min(ans1, ans2))