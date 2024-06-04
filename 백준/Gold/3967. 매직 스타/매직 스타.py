import copy
from itertools import permutations

star = []
for _ in range(5):
    star.append([*map(str, input().rstrip())])

test = [star[0][4],
        star[1][1], star[1][3], star[1][5], star[1][7],
        star[2][2], star[2][6],
        star[3][1], star[3][3], star[3][5], star[3][7],
        star[4][4]]

nums = [i+1 for i in range(12)]
for i in range(12):
    if test[i] == 'x':
        test[i] = 0
    else:
        v = ord(test[i]) - 64
        test[i] = v
        nums.remove(v)

P = permutations(nums, len(nums))
for p in P:
    test2 = copy.deepcopy(test)
    i = 0
    for n in p:
        while test2[i] != 0:
            i += 1
        test2[i] = n

    if (test2[0]+test2[2]+test2[5]+test2[7] == 26
            and test2[7]+test2[8]+test2[9]+test2[10] == 26
            and test2[0]+test2[3]+test2[6]+test2[10] == 26
            and test2[1]+test2[2]+test2[3]+test2[4] == 26
            and test2[1]+test2[5]+test2[8]+test2[11] == 26
            and test2[4]+test2[6]+test2[9]+test2[11] == 26):
        answer = [chr(t+64) for t in test2]
        star[0][4] = answer[0]
        star[1][1] = answer[1]
        star[1][3] = answer[2]
        star[1][5] = answer[3]
        star[1][7] = answer[4]
        star[2][2] = answer[5]
        star[2][6] = answer[6]
        star[3][1] = answer[7]
        star[3][3] = answer[8]
        star[3][5] = answer[9]
        star[3][7] = answer[10]
        star[4][4] = answer[11]
        for i in range(5):
            print(''.join(star[i]))
        break