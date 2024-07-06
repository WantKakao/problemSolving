import sys
# from collections import deque
input = sys.stdin.readline

n = int(input())
month_to_day = [0, 0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]
flower = []
# s2 = 개화 시기, e2 = 낙화 시기
for _ in range(n):
    s1, s2, e1, e2 = map(int, input().split())
    s2 += month_to_day[s1]
    e2 += month_to_day[e1]
    flower.append((s2, e2))

flower.sort()
i = 0
ans = 0
temp = 0
start = 60
end = 335
# q = deque(flower)
# while q:
#     s, e = q.popleft()
#     if s <= start:
#         if e > temp:
#             temp = e
#     else:
#         ans += 1
#         start = temp
#         temp = max(e, temp)

while i < n and temp < end:
    s, e = flower[i]
    if s > start:
        if s <= temp:
            ans += 1
            start = temp
        else:
            break
    temp = max(e, temp)
    i += 1

if temp < end:
    print(0)
else:
    print(ans+1)