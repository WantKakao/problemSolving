import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = list(map(int, input().rstrip()))
    flag = False
    for i in range(len(n)-1, 0, -1):
        if n[i] > n[i-1]:
            l = n[i:]
            l.sort()
            for j in range(len(l)):
                if l[j] > n[i-1]:
                    l[j], n[i-1] = n[i-1], l[j]
                    break
            l.sort()
            flag = True
        if flag:
            break
    if not flag:
        print('BIGGEST')
    else:
        new_n = n[:i] + l
        print("".join(map(str, new_n)))