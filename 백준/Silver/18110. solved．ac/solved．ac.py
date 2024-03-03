import heapq

n = int(input())
if n == 0:
    print(0)
else:
    difficulty = []
    for _ in range(n):
        heapq.heappush(difficulty, int(input()))
    if (3/20)*n-0.5 < int((3/20)*n):
        cut = int((3 / 20) * n)
    else:
        cut = int((3 / 20) * n) + 1
    for _ in range(cut):
        heapq.heappop(difficulty)
    addSum = 0
    for i in range(n-(2*cut)):
        add = heapq.heappop(difficulty)
        addSum += add
    if addSum/(n-(2*cut))-0.5 < int(addSum/(n-(2*cut))):
        print(int(addSum/(n-(2*cut))))
    else:
        print(int(addSum/(n-(2*cut))) + 1)