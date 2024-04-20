vowel = ['a', 'i', 'o', 'u', 'e']
while 1:
    pwd = input()

    if pwd == 'end':
        break

    acceptable = 1
    count = 0
    for v in vowel:
        if v not in pwd:
            count += 1
    if count == 5:
        acceptable = 0

    for i in range(len(pwd) - 2):
        if ((pwd[i] in vowel and pwd[i+1] in vowel and pwd[i+2] in vowel)
                or (pwd[i] not in vowel and pwd[i+1] not in vowel and pwd[i+2] not in vowel)):
            acceptable = 0

    for i in range(len(pwd) - 1):
        if pwd[i] == pwd[i+1] and (pwd[i] != 'e' and pwd[i] != 'o'):
            acceptable = 0

    if acceptable:
        print(f"<{pwd}> is acceptable.")
    else:
        print(f"<{pwd}> is not acceptable.")
