n = int(input())
words = []
for _ in range(n):
    words.append(input())
    
ans = 0
for i in range(n):
    w = words[i]
    set_w = set()
    for k in range(97, 123):
        temp = [idx for idx, val in enumerate(w) if val == chr(k)]
        set_w.add(tuple(temp))
    for j in range(i+1, n):
        w2 = words[j]
        set_w2 = set()
        for k in range(97, 123):
            temp = [idx for idx, val in enumerate(w2) if val == chr(k)]
            set_w2.add(tuple(temp))
        if set_w == set_w2:
            ans += 1
            
print(ans)