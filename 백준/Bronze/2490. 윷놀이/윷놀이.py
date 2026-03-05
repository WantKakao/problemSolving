l1 = list(map(int, input().split()))
l2 = list(map(int, input().split()))
l3 = list(map(int, input().split()))

def s(l):
    if sum(l) == 3:
        print('A')
    elif sum(l) == 2:
        print('B')
    elif sum(l) == 1:
        print('C')
    elif sum(l) == 0:
        print('D')
    else:
        print('E')
        
s(l1)
s(l2)
s(l3)