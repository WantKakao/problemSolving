a = input()
b = input()
c = input()

if a[0].isdigit():
    num = int(a)+3
elif b[0].isdigit():
    num = int(b)+2
else:
    num = int(c)+1

if num % 3 == 0:
    if num % 5 == 0:
        print('FizzBuzz')
    else:
        print('Fizz')
elif num % 5 == 0:
    print('Buzz')
else:
    print(num)