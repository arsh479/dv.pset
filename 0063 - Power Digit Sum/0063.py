def findsumofdigits(f):
    i = 0
    c = 0
    strlist = list(str(f))
    intlist = list(map(int, strlist))
    for i in range (0, len(str(f))):
        c = intlist[i] +c
        i = i+1
    return (c)


print('Enter a number and then the power to find sum of digits in the respective output')
print(end = '\n')
x = int(input('Enter a number: '))
y = int(input('Enter a power: '))
o = (x**y)
sum = findsumofdigits(o)
print(sum)
