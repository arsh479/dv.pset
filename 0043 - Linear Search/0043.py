i = 0
while i == 0:
    print(end = '\n')
    print('Enter a list 5 numbers')
    x1 = int(input('Enter first number : '))
    x2 = int(input('Enter second number : '))
    x3 = int(input('Enter third number : '))
    x4 = int(input('Enter fourth number : '))
    x5 = int(input('Enter fifth number : '))


    x = int(input('enter number for search: '))

    if (x == x1) or (x == x2) or (x == x3) or (x == x4) or (x == x5):# checks for each of x1,x2... till one is equal to x then print true or false. Hence linear search
        print('number is there')
    else:
        print('not there')
    continue
