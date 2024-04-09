word = input()
w = len(word)

arr = ['z']
for i in range(w-2):
    for j in range(i+1, w-1):
        new_word = word[i::-1]
        new_word += word[j:i:-1]
        new_word += word[:j:-1]
        arr.append(new_word)
        arr.sort()
        arr.pop(-1)

print(arr[0])