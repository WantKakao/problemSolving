month, day = map(int, input().split())
l = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

n = sum(l[:month]) + day
k = n % 7

if k == 1:
    print('MON')
elif k == 2:
    print('TUE')
elif k == 3:
    print('WED')
elif k == 4:
    print('THU')
elif k == 5:
    print('FRI')
elif k == 6:
    print('SAT')
else:
    print('SUN')
