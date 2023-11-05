import heapq

n = int(input())
cards = []
for _ in range(n):
    heapq.heappush(cards, int(input()))

ans = 0
while len(cards) > 1:
    card1 = heapq.heappop(cards)
    card2 = heapq.heappop(cards)
    card_dummy = card1 + card2
    ans += card_dummy
    heapq.heappush(cards, card_dummy)

print(ans)
