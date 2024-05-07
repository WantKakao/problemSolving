S = input()

l = len(S)
temp = ''

for i in range(l-1):
    temp += S[i]
    if temp[::-1] < temp:
        if S[i+1] <= temp[-1]:
            pass
        else:
            temp = temp[::-1]

    if temp[::-1] > temp:
        if S[i+1] <= temp[0]:
            temp = temp[::-1]
        else:
            pass

temp += S[l-1]
if temp[0] > temp[l-1]:
    temp = temp[::-1]
print(temp)