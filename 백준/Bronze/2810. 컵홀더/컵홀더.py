n = int(input())
l = input()
c = max(l.count('L')//2 - 1, 0)
print(n-c)