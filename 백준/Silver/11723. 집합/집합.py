import sys
input = sys.stdin.readline

n = int(input())
s = set()
for _ in range(n):
    command = input().split()
    if command[0] == 'add':
        s.add(int(command[1]))
    elif command[0] == 'remove':
        if int(command[1]) in s:
            s.remove(int(command[1]))
    elif command[0] == 'check':
        if int(command[1]) in s:
            print(1)
        else:
            print(0)
    elif command[0] == 'toggle':
        if int(command[1]) in s:
            s.remove(int(command[1]))
        else:
            s.add(int(command[1]))
    elif command[0] == 'all':
        s = set(i for i in range(1, 21))
    else:
        s = set()
