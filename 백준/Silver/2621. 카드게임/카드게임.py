card = []
number = []
for _ in range(5):
    c, n = map(str, input().split())
    card.append(c)
    number.append(int(n))

count = [number.count(i) for i in range(10)]
number.sort()

if len(set(card)) == 1:
    if number[4] - number[0] == 4:
        print(900+number[4])
    else:
        print(600+number[4])
else:
    M = max(count)
    if M == 4:
        idx = count.index(M)
        print(800+idx)
    elif M == 3:
        idx = count.index(M)
        if len(set(number)) == 2:
            idx2 = count.index(2)
            print(700+(10*idx)+idx2)
        else:
            print(400+idx)
    elif M == 2:
        if len(set(number)) == 3:
            print(300+(number[3]*10)+number[1])
        else:
            idx = count.index(M)
            print(200+idx)
    else:
        if number[0]+4 == number[4]:
            print(500+number[4])
        else:
            print(100+number[4])

           