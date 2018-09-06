i = 1
import random
while i == 1:
    wow1 = random.randint(0, 10**2)
    wow2 = random.randint(0, 10**2)
    wow3 = random.randint(0, 10**2)
    wow4 = random.randint(0, 10**2)
    wow5 = random.randint(0, 10**2)

    x =  input('please press enter: ')

    if (wow1 == wow2) and (wow2 == wow3) and (wow3 == wow4) and (wow4 == wow5)\
    and (wow1 == wow3) and (wow1 == wow4) and (wow1 == wow5) and (wow2 == wow4) and\
     (wow2 == wow5) and (wow3 == wow5) and (wow4 == wow5) :
     continue

    elif ("" in x) :
        print(wow1)
        print(wow2)
        print(wow3)
        print(wow4)
        print(wow5)
        print(end = '\n')
        print('press ctrl + c to exit')
        print(end = '\n')
