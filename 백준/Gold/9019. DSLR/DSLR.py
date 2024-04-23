from collections import deque
import sys
input = sys.stdin.readline


def d(num):
    return (num * 2) % 10000


def s(num):
    return 9999 if num == 0 else num - 1


def l(num):
    temp = num * 10
    return (temp % 10000) + (temp // 10000)


def r(num):
    temp = num // 10
    return ((num % 10) * 1000) + temp


t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    q = deque([(a, '')])
    visited = [False for _ in range(10000)]
    while True:
        number, command = q.popleft()
        if not visited[number]:
            visited[number] = True
            a1, a2, a3, a4 = d(number), s(number), l(number), r(number)
            if a1 == b:
                print(command+'D')
                break
            elif a2 == b:
                print(command+'S')
                break
            elif a3 == b:
                print(command+'L')
                break
            elif a4 == b:
                print(command+'R')
                break
            q.append((a1, command+'D'))
            q.append((a2, command+'S'))
            q.append((a3, command+'L'))
            q.append((a4, command+'R'))
