n = int(input())
l = []
for _ in range(n):
    l.append(int(input()))
    
ans1, ans2, temp1, temp2 = 0, 0, 0, 0
for i in range(n):
    if l[i] > temp1:
        ans1 += 1
        temp1 = l[i]
    if l[-1-i] > temp2:
        ans2 += 1
        temp2 = l[-1-i]
        
print(ans1)
print(ans2)