n, m = map(int, input().split())
boxes = []
for _ in range(n):
    boxes.append(list(map(int, input().split())))

have_to_move = -1
already_box = [False for _ in range(m)]
for box in boxes:
    cnt = box.count(0)
    if cnt == m-1:
        for i in range(m):
            if box[i] != 0:
                if not already_box[i]:
                    have_to_move -= 1
                    already_box[i] = True
    if cnt == m:
        have_to_move -= 1
    have_to_move += 1

print(max(have_to_move, 0))