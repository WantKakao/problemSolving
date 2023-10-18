import sys
n = int(input())
q = []
for _ in range(n):
    i = sys.stdin.readline().rstrip()
    if i == 'pop':
        if q:
            print(q.pop())
        else:
            print(-1)
    elif i == 'size':
        print(len(q))
    elif i == 'empty':
        if q:
            print(0)
        else:
            print(1)
    elif i == 'top':
        if q:
            print(q[-1])
        else:
            print(-1)
    else:
        a, b = i.split()
        q.append(int(b))