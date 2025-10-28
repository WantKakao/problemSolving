import sys

In, Out = map(str, input().split('='))
In1, In2 = In.split('+')
Input1, Input2, Output = [0, 0, 0], [0, 0, 0], [0, 0, 0]

def func(e, l):
    if e == 'C':
        l[0] += 1
    elif e == 'H':
        l[1] += 1
    elif e == 'O':
        l[2] += 1

for i in range(len(In1)):
    if In1[i].isdigit():
        for j in range(int(In1[i])-1):
            func(In1[i-1], Input1)
    elif In1[i] == 'C' or In1[i] == 'H' or In1[i] == 'O':
        func(In1[i], Input1)
        
for i in range(len(In2)):
    if In2[i].isdigit():
        for j in range(int(In2[i])-1):
            func(In2[i-1], Input2)
    elif In2[i] == 'C' or In2[i] == 'H' or In2[i] == 'O':
        func(In2[i], Input2)
        
for i in range(len(Out)):
    if Out[i].isdigit():
        for j in range(int(Out[i])-1):
            func(Out[i-1], Output)
    elif Out[i] == 'C' or Out[i] == 'H' or Out[i] == 'O':
        func(Out[i], Output)
        
for i in range(1, 11):
    for j in range(1, 11):
        for k in range(1, 11):
            if all(i*a + j*b == k*c for a, b, c in zip(Input1, Input2, Output)):
                print(i, j, k)
                sys.exit()