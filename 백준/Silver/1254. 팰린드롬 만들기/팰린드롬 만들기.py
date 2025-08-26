S = input()

def is_palindrome(x, y):
    for j in range(len(S)-x):
        if x-y-j < 0 or S[x+j] != S[x-y-j]:
            return False
    return True

ans = len(S)*2-1
start = len(S)//2 if len(S)%2 == 0 else len(S)//2+1
for i in range(start, len(S)):
    if S[i] == S[i-2]:
        if is_palindrome(i, 2):
            ans = 2*i-1
            break
    if S[i] == S[i-1]:
        if is_palindrome(i, 1):
            ans = 2*i
            break
    
print(ans)