a, b = map(str, input().split())
m1, M1, m2, M2 = '', '' , '', ''
for i in a:
    if i == '5' or i == '6':
        m1 += '5'
        M1 += '6'
    else:
        m1 += i
        M1 += i
for j in b:
    if j == '5' or j == '6':
        m2 += '5'
        M2 += '6'
    else:
        m2 += j
        M2 += j
m1, M1, m2, M2 = int(m1), int(M1), int(m2), int(M2)
k1, k2 = m1+m2, M1+M2
print(k1, k2)