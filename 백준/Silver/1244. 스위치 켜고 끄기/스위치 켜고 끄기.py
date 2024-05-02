import sys
input = sys.stdin.readline

n = int(input())
switch = [0] + list(map(int, input().split()))
m = int(input())
for _ in range(m):
    a, b = map(int, input().split())

    if a == 1:
        for i in range(b, n+1, b):
            switch[i] = 0 if switch[i] == 1 else 1

    else:
        switch[b] = 0 if switch[b] == 1 else 1
        i = 1
        while b-i > 0 and b+i <= n and switch[b-i] == switch[b+i]:
            switch[b-i] = 0 if switch[b-i] == 1 else 1
            switch[b+i] = 0 if switch[b+i] == 1 else 1
            i += 1

for i in range(5):
    print(' '.join(map(str, switch[20*i+1:20*(i+1)+1])))
