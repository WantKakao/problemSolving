n = int(input())
students = []
for _ in range(n):
    students.append(list(map(int, input().split())))

friends = [set() for _ in range(n)]
for k in range(5):
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            if students[i][k] == students[j][k]:
                friends[i].add(j)

for i in range(n):
    friends[i] = len(friends[i])
print(friends.index(max(friends))+1)