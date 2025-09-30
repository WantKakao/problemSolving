n = int(input())
words = []
for _ in range(n):
    w = input()
    l = len(w)
    ww = w + w
    already_in = False
    
    for i in range(l):
        word = ww[i:i+l]
        if word in words:
            already_in = True
    if not already_in:
        words.append(w)
        
print(len(words))