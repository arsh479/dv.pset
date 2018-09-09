x = int(input('enter number: '))
n=0

i = 0
for n in range(1,x+1):
    if n%7 == 0:
        i = i + 1
print(i)
