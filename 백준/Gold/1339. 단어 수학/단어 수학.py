n = int(input())
l = [input() for _ in range(n)]
count = dict()
for w in l:
    len_w = len(w)
    for i in range(len_w):
        if w[i] in count.keys():
            count[w[i]] += 10**(len(w)-i-1)
        else:
            count[w[i]] = 10**(len(w)-i-1)
            
count_l = list(count.items())
count_l.sort(key=lambda x:-x[1])
new_l = dict()
for i in range(len(count_l)):
    new_l[count_l[i][0]] = (9-i)

ans = 0
for w in l:
    new_w = ''
    for s in w:
        new_w += str(new_l[s])
    ans += int(new_w)
print(ans)