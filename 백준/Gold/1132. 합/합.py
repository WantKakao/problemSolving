n = int(input())
nums = [[0 for _ in range(10)] for _ in range(12)]
heads = set()
for _ in range(n):
    string = input()
    for i in range(len(string)):
        num = ord(string[-1-i]) - 65
        nums[-1-i][num] += 1
    heads.add(ord(string[0]) - 65)

alphabets = []
for j in range(10):
    alphabet = 0
    for i in range(12):
        alphabet += nums[i][j] * (10 ** (11-i))
    alphabets.append((alphabet, j))

ans = 0
alphabets.sort()
available_num = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

for i in range(10):
    start = 1 if alphabets[i][1] in heads else 0
    for j in range(start, 10):
        if available_num[j] == 1:
            ans += alphabets[i][0] * j
            available_num[j] -= 1
            break
            
print(ans)