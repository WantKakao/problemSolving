import sys

for line in sys.stdin:
    n = int(line)
    
    if n % 2 == 0 or n % 5 == 0:
        print(0)
        continue
    
    num = 1
    length = 1
    
    while num % n != 0:
        num = (num * 10 + 1) % n
        length += 1
    
    print(length)
