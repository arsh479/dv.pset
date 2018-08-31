x = input('input first fraction numerator: ')   #make numerator and denominator input seperately
y = input('input first fraction denominator: ')
xx = input('input second fraction numerator: ')
yy = input('input second fraction denominator: ')

xy = int(x)/int(y)  # finding out LCM for equal and unequal denominator seperately
xyxy = int(xx)/int(yy)
z = int(x)*int(yy) + int(xx)*int(y)
zz = int(yy)*int(y)
x_ = int(x) + int(xx)
if y != yy:

    print(str(z) + '/' + str(zz))

elif y == yy:
    print(str(x_) + '/' + str(yy))
