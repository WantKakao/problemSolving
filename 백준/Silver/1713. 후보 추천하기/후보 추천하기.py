n = int(input())
m = int(input())
rec = list(map(int, input().split()))
photo = []
photo_count = []

for r in rec:
    if r not in photo:
        if len(photo) < n:
            photo.append(r)
            photo_count.append(1)
        else:
            idx = photo_count.index(min(photo_count))
            photo.pop(idx)
            photo_count.pop(idx)
            photo.append(r)
            photo_count.append(1)
    else:
        idx = photo.index(r)
        photo_count[idx] += 1
        
photo.sort()
print(*photo)