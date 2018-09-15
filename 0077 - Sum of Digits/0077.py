def findsumofdigits(x):
    i = 0
    c = 0
    strlist = list(str(x))
    intlist = list(map(int, strlist))
    for i in range (0, len(str(x))):
        c = intlist[i] +c
        i = i+1
    print(c)

findsumofdigits(123456)
