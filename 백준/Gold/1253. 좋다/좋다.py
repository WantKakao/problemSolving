n = int(input())
numbers = list(map(int, input().split()))
numbers.sort()

ans = 0
for i in range(n):
    temp = numbers[:i] + numbers[i+1:]
    found = False
    for j in range(n-1):
        s, e = 0, n-1
        while s < e:
            m = (s + e) // 2
            if m != j and temp[j] + temp[m] == numbers[i]:
                ans += 1
                found = True
                break
            elif temp[j] + temp[m] < numbers[i]:
                s = m + 1
            else:
                e = m
        if found:
            break

print(ans)
