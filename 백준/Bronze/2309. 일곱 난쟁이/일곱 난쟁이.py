# import itertools   라이브러리 사용
import sys
input = sys.stdin.readline
tall = []

for _ in range(9):
    tall.append(int(input().strip()))

possible = []
temp = []

def combination(n, r, s):
    if len(temp) == r:
        possible.append([t for t in temp])
    for i in range(s, n):
        temp.append(tall[i])
        combination(n, r, i+1)
        del temp[-1]
    return

combination(9, 7, 0)

# possible = itertools.combinations(tall, 7)
for p in possible:
    if sum(p) == 100:
        for dwarf in sorted(p):
            print(dwarf)
        break