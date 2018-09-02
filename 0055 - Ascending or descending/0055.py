import random

i = 1
print('                                                    Welcome to find ascending or descending numbers')
print(end ='\n')


while i == 1:
    x = int(input('Enter number: ')) #5 different inputs so to set conditions for each input with every other input
    y = int(input('Enter number: '))
    z = int(input('Enter number: '))
    a = int(input('Enter number: '))
    b = int(input('Enter number: '))

    if (x < y) and (y < z) and (z < a) and (a < b): #setting basic ascending and descending criteria for each input
        print(end='\n')
        print("numbers are Ascending")
        print('Press ctrl + c to exit')
        print(end='\n')
        continue
    elif (x > y) and (y > z) and (z > a) and (a > b):
        print(end='\n')
        print('numbers are Descending')
        print('Press ctrl + c to exit')
        print(end='\n')
        continue

    else:
        print(end='\n')  #setting a neither Asc or Desc case
        print('none')
        print('Press ctrl + c to exit')
        print(end='\n')
        continue
