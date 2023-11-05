length, width = map(int, input().split())
cut = int(input())
width_cut = []
length_cut = []
for _ in range(cut):
    mode, location = map(int, input().split())
    if mode == 0:
        width_cut.append(location)
    else:
        length_cut.append(location)
width_cut.append(width)
length_cut.append(length)
width_cut.sort()
length_cut.sort()

x = 0
M = 0
for i in width_cut:
    y = 0
    for j in length_cut:
        M = max(M, (i-x)*(j-y))
        y = j
    x = i

print(M)
