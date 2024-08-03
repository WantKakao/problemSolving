w = input()
flag = 1
for i in range(len(w)//2):
    if w[i] != w[len(w)-i-1]:
        flag = 0
        break
if not flag:
    print(0)
else:
    print(1)