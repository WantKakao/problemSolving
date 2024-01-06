from itertools import combinations
import sys
input = sys.stdin.readline

while 1:
    info = [*map(int, input().split())]
    if info == [0]:
        break
    else:
        n, nums = info[0], info[1:]
        combi = list(combinations(nums, 6))
        combi.sort()
        for i in combi:
            for j in i:
                print(j, end=' ')
            print()
    print()