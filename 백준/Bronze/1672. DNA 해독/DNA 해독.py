n = int(input())
s = input().rstrip()

def add(a, b):
    if (a==b=='A') or (a=='A' and b=='C') or (a=='G' and b=='T') or (a=='C' and b=='A') or (a=='T' and b=='G'):
        return 'A'
    if (a=='A' and b=='G') or (a=='G' and b=='A') or (a==b=='C'):
        return 'C'
    if (a=='A' and b=='T') or (a==b=='G') or (a=='C' and b=='T') or (a=='T' and b=='A') or (a=='T' and b=='C'):
        return 'G'
    if (a=='G' and b=='C') or (a=='C' and b=='G') or (a==b=='T'):
        return 'T'

An, An1 = s[-1], s[-1]
for i in range(n-1):
    An1 = s[-i-2]
    An = add(An, An1)
print(An)