


def reversesumequality(x):
    def findsumofdigits(f):
        i = 0
        c = 0
        strlist = list(str(f))
        intlist = list(map(int, strlist))
        for i in range (0, len(str(f))):
            c = intlist[i] +c
            i = i+1
        return (c)
    i = 0
    ls= []
    ls2 = []
    for i in range(0, (len(x))):
        ls.append(x[i])
    for i in range(0, (len(x))):
        d = len(x) - 1
        c = ls[d-i]
        ls2.append(c)
        ls3 = list(map(int, ls2))
        y = ''.join(map(str, ls3))
        intls2 = list(map(int, ls))
        z = ''.join(map(str, intls2))
    d = findsumofdigits(y)
    dd = findsumofdigits(z)
    if d == dd:
        print('true')

    else:
        print('false')

reversesumequality(str(12345876543))
