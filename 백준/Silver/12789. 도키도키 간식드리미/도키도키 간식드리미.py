x = int(input())
l = list(map(int, input().split()))
l1 = list(reversed(l))
l2 = []
a = 1

for i in range(x):
    while l2 and l2[-1] == a:
        l2.pop()
        a += 1
    p = l1.pop()
    if p == a:
        a += 1
    else:
        l2.append(p)
while l2:
    p = l2.pop()
    if p == a:
        a += 1
if a == x+1:
    print("Nice")
else:
    print('Sad')