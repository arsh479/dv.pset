def findsumofdigits(f):
    i = 0
    c = 0
    strlist = list(str(f))
    intlist = list(map(int, strlist))
    for i in range (0, len(str(f))):
        c = intlist[i] +c
        i = i+1
    return (c)
ls = []
i =0
mul = 1
x = int(input('Enter a number: '))
for i in range (0,x):
    c = (x-i)
    mul = mul * c
    f = findsumofdigits(mul)
print(f)
