i = 1
while True:
    n = int(input())
    if n == 0:
        break
    if n % 2 == 0:
        print(f'{i}. even {n//2}')
    else:
        print(f'{i}. odd {(n-1)//2}')
    i += 1