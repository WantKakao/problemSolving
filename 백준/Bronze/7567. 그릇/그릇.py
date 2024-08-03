l = [0] + list(map(str, input()))
lng = 0
for i in range(1, len(l)):
    if l[i] != l[i-1]:
        lng += 10
    else:
        lng += 5
print(lng)