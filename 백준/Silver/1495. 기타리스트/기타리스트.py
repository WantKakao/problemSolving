from collections import deque
songs, startVolume, maxVolume = map(int, input().split())
volumes = [*map(int, input().split())]

# QUEUE 메모리초과
# q = deque()
# q.append((startVolume, 0))
# while q:
#     v, i = q.popleft()
#     if i == songs:
#         break
#     if v + volumes[i] <= maxVolume:
#         q.append((v + volumes[i], i + 1))
#     if v - volumes[i] >= 0:
#         q.append((v - volumes[i], i + 1))
# if q:
#     print(max(q)[0])
# else:
#     print(-1)

# DP 메모리초과
dp = []
dp.append(startVolume)
for i in range(1, songs+1):
    temp = []
    for v in dp:
        plus = v + volumes[i-1]
        minus = v - volumes[i-1]
        if plus <= maxVolume and plus not in temp:
            temp.append(v + volumes[i-1])
        if minus >= 0 and minus not in temp:
            temp.append(v - volumes[i-1])
    dp = temp
    if not dp:
        break

if dp:
    print(max(dp))
else:
    print(-1)