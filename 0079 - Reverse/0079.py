def reverse(x):
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
    print(''.join(map(str, ls3)))






reverse(str(759757957955579))
