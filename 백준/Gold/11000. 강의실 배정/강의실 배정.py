import heapq
n = int(input())
room = []
classes = []
for _ in range(n):
    start, end = map(int, input().split())
    heapq.heappush(classes, (start, end))

while classes:
    s, e = heapq.heappop(classes)
    if not room or room[0] > s:
        heapq.heappush(room, e)
    else:
        heapq.heappop(room)
        heapq.heappush(room, e)

print(len(room))