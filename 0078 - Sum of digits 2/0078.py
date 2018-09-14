def findsumofdigits(x):
    i = 0
    c = 0
    strlist = list(str(x))
    intlist = list(map(int, strlist))
    for i in range (0, len(str(x))):
        c = intlist[i] +c
        i = i+1
    return c


x = int(input('Enter first number: '))
y = int(input('Enter second number: '))
if findsumofdigits(x) == findsumofdigits(y):
    print('1')
else:
    print('0')
