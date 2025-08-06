n = int(input())
friends = []
for _ in range(n):
    friends.append(list(input()))
    
two_friend = 0
for i in range(n):
    i_friend = 0
    for j in range(n):
        if i == j:
            continue
        elif friends[i][j] == 'Y':
            i_friend += 1
        else:
            common_friend = 0
            for k in range(n):
                if friends[i][k] == friends[j][k] == 'Y':
                    common_friend = 1
            if common_friend:
                i_friend += 1
    two_friend = max(two_friend, i_friend)
print(two_friend)