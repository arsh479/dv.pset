ls = []
i = 0
x = int(input('enter number: '))
for i in range(0,x): #instead of using the formula n! = n*(n-1) i removed the first part and used (n-i) where i goes from 0 to n-1
    c = (x-i)# sequence is (100-i1) = 100-0 = 100 , 100-i2 = 100-1 =99...and so on till x which is till i99
    i = i+1
    ls.append(c)
    d = sum(ls)
print(d)
