n = input()
ans = 0
for l in range(1, (len(n)//2)+1):
    for i in range(len(n)-(2*l)+1):
        left_sum = sum(int(ch) for ch in n[i:i+l])
        right_sum = total = sum(int(ch) for ch in n[i+l:i+(2*l)])
        if left_sum == right_sum:
            ans = 2*l
print(ans)