from collections import Counter

n = int(input())
books = []
for _ in range(n):
    books.append(input())
    
c = Counter(books)
sorted_items = sorted(c.items(), key=lambda x: (-x[1], x[0]))
print(sorted_items[0][0])