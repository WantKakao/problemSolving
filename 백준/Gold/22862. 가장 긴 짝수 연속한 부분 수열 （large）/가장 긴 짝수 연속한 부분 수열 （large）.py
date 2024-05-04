n, k = map(int, input().split())
S = list(map(int, input().split()))

even = True if S[0] % 2 == 0 else False
continuous_odd_even = []
count = 1

for i in range(1, n):
    if S[i-1] % 2 == S[i] % 2:
        count += 1
    else:
        continuous_odd_even.append(count)
        count = 1
continuous_odd_even.append(count)

answer, temp, start = 0, 0, 0
# 첫째항이 짝수일 때 짝수번째 항은 짝수
if even:
    for i in range(len(continuous_odd_even)):
        if i % 2 == 0:
            temp += continuous_odd_even[i]
            if answer < temp:
                answer = temp
        else:
            k -= continuous_odd_even[i]
            while k < 0:
                temp -= continuous_odd_even[start]
                k += continuous_odd_even[start+1]
                start += 2

else:
    for i in range(1, len(continuous_odd_even)):
        if i % 2 == 1:
            temp += continuous_odd_even[i]
            if answer < temp:
                answer = temp
        else:
            k -= continuous_odd_even[i]
            while k < 0:
                temp -= continuous_odd_even[start+1]
                k += continuous_odd_even[start+2]
                start += 2

print(answer)
