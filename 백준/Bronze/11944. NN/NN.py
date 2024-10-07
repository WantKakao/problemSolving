n, m = map(str, input().split())
l = min(int(n)*len(n), int(m))
arr = [n[i%len(n)] for i in range(l)]
print(''.join(arr))