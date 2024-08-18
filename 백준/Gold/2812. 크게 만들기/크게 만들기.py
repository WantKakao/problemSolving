n, k = map(int, input().split())
num = input()

q = []
for n in num:
    while q and q[-1] < int(n) and k > 0:
        q.pop()
        k -= 1
    q.append(int(n))

while k > 0:
    q.pop()
    k -= 1

for i in q:
    print(i, end='')