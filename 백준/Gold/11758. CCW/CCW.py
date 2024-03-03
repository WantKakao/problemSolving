x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())

if (x1 == x2 == x3) or (y1 == y2 == y3) or ((y2-y1)/(x2-x1) == (y3-y2)/(x3-x2)):
    print(0)
else:
    if x2 == x1:
        if (x3 < x2 and y2 > y1) or (x3 > x2 and y2 < y1):
            print(1)
        else:
            print(-1)
    # (y2 - y1) / (x2 - x1)
    elif x2 > x1:
        if (y2-y1)/(x2-x1) > (y3-y2)/(x3-x2):
            if x3 > x2:
                print(-1)
            else:
                print(1)
        else:
            if x3 > x2:
                print(1)
            else:
                print(-1)
    else:
        if (y2-y1)/(x2-x1) > (y3-y2)/(x3-x2):
            if x3 < x2:
                print(-1)
            else:
                print(1)
        else:
            if x3 < x2:
                print(1)
            else:
                print(-1)