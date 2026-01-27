def to_base36(n):
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if n == 0:
        return "0"

    res = ""
    while n > 0:
        n, r = divmod(n, a)
        res = digits[r] + res
    return res

n, a = map(int, input().split())
print(to_base36(n))