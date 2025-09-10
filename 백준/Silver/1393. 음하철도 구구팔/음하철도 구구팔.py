xs, ys = map(int, input().split())
xe, ye, dx, dy = map(int, input().split())

dist = 1e9
ans = [0, 0]
if dx == 0:
    print(xe, ys)
else:
    for i in range(-200, 201):
        for j in range(-200, 201):
            temp = (xs-i)**2 + (ys-j)**2
            if temp < dist and (dy/dx)*(i-xe) == (j-ye) and (i-xe)*dx >= 0 and (j-ye)*dy >= 0:
                dist = temp
                ans = [i, j]
    
    print(ans[0], ans[1])