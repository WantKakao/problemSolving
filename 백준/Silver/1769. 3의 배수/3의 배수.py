import sys
input = sys.stdin.readline().strip

n = int(input())
i = 0
while True:
    if n < 10:
        print(i)
        ans = 'YES' if n % 3 == 0 else 'NO'
        print(ans)
        break
        
    n = sum(int(c) for c in str(n))
    i += 1