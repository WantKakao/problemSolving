import sys
input = sys.stdin.readline
t = int(input())
l = []
for _ in range(t):
    n = input().rstrip()
    if n[0] == '1':
        a, b = n.split()
        l.append(b)
    elif n[0] == '2':
        if len(l) == 0:
            print(-1)
        else:
            print(l.pop())
    elif n[0] == '3':
        print(len(l))
    elif n[0] == '4':
        if len(l) == 0:
            print(1)
        else:
            print(0)
    elif n[0] == '5':
        if len(l)== 0:
            print(-1)
        else:
            print(l[-1])