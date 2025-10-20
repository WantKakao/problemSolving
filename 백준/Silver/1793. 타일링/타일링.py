tiles = [1 for _ in range(251)]
tiles[1] = 1
tiles[2] = 3
for i in range(3, 251):
    tiles[i] = 2 * tiles[i-2] + tiles[i-1]

while True:
    try:
        n = int(input())
        print(tiles[n])
    except: break    