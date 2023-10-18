import sys
input = sys.stdin.readline

n, k = map(int, input().split())
peoples = [i+1 for i in range(n)]
l = len(peoples)
s = 0
# 1. k * i index 의 숫자를 빼낸다
# 2. k * i > old_peoples 이면 k * i % len(old_peoples)
# 2-2. 이때 len 을 재정의
# 3. new_peoples 의 k * i % len(old_peoples) index 의 숫자를 빼낸다

print('<', end='')
for _ in range(n-1):
    # print(peoples)
    s += k - 1
    if s > l-1:
        s %= l
    print(peoples.pop(s), end=', ')
    l = len(peoples)
print(f'{peoples.pop()}>')