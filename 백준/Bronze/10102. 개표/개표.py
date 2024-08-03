n = int(input())
l = list(map(str, input()))
a = l.count('A')
b = l.count('B')
if a > b:
    print('A')
elif a < b:
    print('B')
else:
    print('Tie')