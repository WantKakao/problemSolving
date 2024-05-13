import heapq

n, m = map(int, input().split())
cards = [*map(int, input().split())]

cards.sort()
for _ in range(m):
    a = cards.pop(0)
    b = cards.pop(0)
    for _ in range(2):
        cards.append(a+b)
    cards.sort()

print(sum(cards))