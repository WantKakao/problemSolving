top, start, end, up, down = map(int, input().split())

ans = 0
if start == end:
    print(0)
elif down == 0 and end > start:
    if up != 0 and (end - start) % up == 0:
        print((end - start) // up)
    else:
        print("use the stairs")
elif up == 0 and start > end:
    if down != 0 and (start - end) % down == 0:
        print((start - end) // down)
    else:
        print("use the stairs")
elif up != 0 and down != 0:
    for _ in range(1000000):
        if start == end:
            break
        elif end > start and start + up <= top:
            start += up
        elif end < start and start - down > 0:
            start -= down
        elif end > start and start - down > 0:
            start -= down
        elif end < start and start + up <= top:
            start += up
        ans += 1
    if ans < 1e6:
        print(ans)
    else:
        print("use the stairs")
else:
    print("use the stairs")