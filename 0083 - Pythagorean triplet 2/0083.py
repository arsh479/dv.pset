#import random
print('                                                                   Welcome to Find your pythagorean triplet')
print(end='\n')
print('A pythagorean triplet is when the condition a^2 + b^2 = c^2 (where c>b>a)')
print(end='\n')
print(end='\n')

i = 1
while i == 1:
    x = int(input ("Please enter digit for a: "))
    y = int(input ("Please enter digit for b: " ))
    z = int(input ( "Please enter digit for c: "))
    if (x**2 + y**2 == z**2) :
        print('Correct, thats a pythagorean triplet')
        print(end = '\n')
        print('press ctrl + c to exit')
        print(end = '\n')
        continue
    else:
        print('thats wrong')
        print(end = '\n')
        print('press ctrl + c to exit')
        print(end = '\n')
        continue
