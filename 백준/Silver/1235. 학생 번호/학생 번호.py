n = int(input())
students = []
for _ in range(n):
    students.append(input()[::-1])

def is_distinguishable(m):
    temp = []
    for s in students:
        if s[:m+1] in temp:
            return False
        temp.append(s[:m+1])
    return True
    
for k in range(len(students[0])):
        if is_distinguishable(k):
            print(k+1)
            break