a, b = map(int, input().split())
i = 1
ans = 0
num_list = []
while b > 0:
    if a-i <= 0 and not num_list:
        num_list.append((a, i))
    if b-i <= 0:
        num_list.append((b, i))
    a -= i
    b -= i
    i += 1
    
for i in range(num_list[0][1], num_list[1][1]+1):
    if i == num_list[0][1]:
        ans += i * (i - num_list[0][0] + 1)
    if i == num_list[1][1]:
        ans += i * (num_list[1][0])
    if i != num_list[0][1] and i != num_list[1][1]:
        ans += i**2
        
if num_list[0][1] == num_list[1][1]:
    ans -= num_list[0][1]**2
print(ans)