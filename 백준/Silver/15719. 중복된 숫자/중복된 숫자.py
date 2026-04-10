import sys

n = int(sys.stdin.readline())
s = (n * (n-1)) // 2

total = 0
num = 0

while True:
    c = sys.stdin.read(1)
    if not c:
        total += num
        break
    
    if c == ' ' or c == '\n':
        total += num
        num = 0
    else:
        num = num * 10 + (ord(c) - 48)

print(total - s)
