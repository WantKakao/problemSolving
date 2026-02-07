a, b = map(int, input().split())
c = int(input())
n = int(input())
if c>=a and ((c-a)*n)>=b:
    print(1)
else:
    print(0)