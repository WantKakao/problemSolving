L, U = map(int, input().split())

def num_sum(str_n):
    ans = 0
    l = len(str_n)
    for i in range(l):
        n = int(str_n[i])
        r = int(str_n[i+1:]) if i != l-1 else 0
        for j in range(1, n):
            ans += (j*(10**(l-1-i)))
        ans += (n*(r+1))
    for i in range(1, l):
        b = int(str_n[:i])
        n = int(str_n[i])
        ans += (45*(10**(l-1-i))*b)
    return ans

L = 1 if L == 0 else L
print(num_sum(str(U)) - num_sum(str(L-1)))