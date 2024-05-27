import sys
input = sys.stdin.readline

n, m = map(int, input().split())
idol = dict()

for _ in range(n):
    group = input().rstrip()
    p = int(input())
    for _ in range(p):
        member = input().rstrip()
        if idol.get(group):
            idol[group].append(member)
        else:
            idol[group] = [member]

for _ in range(m):
    quiz = input().rstrip()
    t = int(input())

    if t:
        for i in idol:
            if quiz in idol[i]:
                print(i)
    else:
        idol[quiz].sort()
        print('\n'.join(idol[quiz]))