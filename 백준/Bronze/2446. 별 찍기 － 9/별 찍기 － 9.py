n = int(input())
for i in range(n):
    blank = i
    star = 2*(n-i)-1
    print(' '*blank+'*'*star)
for j in range(n-2, -1, -1):
    blank = j
    star = 2*(n-j)-1
    print(' '*blank+'*'*star)