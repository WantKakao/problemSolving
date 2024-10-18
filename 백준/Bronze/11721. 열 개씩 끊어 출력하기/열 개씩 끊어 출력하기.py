s = input()
a, b = divmod(len(s), 10)
for i in range(a):
    print(s[i*10:i*10+10])
if b:
    print(s[a*10:])