import sys
input = sys.stdin.readline

n = int(input())
log = {}
for _ in range(n):
    name, action = map(str, input().split())
    if action == 'enter':
        log[name] = 1
    else:
        log[name] = 0

people = []
for key, value in log.items():
    if value == 1:
        people.append(key)

people.sort(reverse=True)
for p in people:
    print(p)
