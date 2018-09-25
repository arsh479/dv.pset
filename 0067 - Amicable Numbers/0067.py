def amicable(a,b):
    sum1 = 0
    sum2 = 0



    for x in range (1,int(a/2)+1):
        if a % x == 0:
            sum1 = sum1 + x



    for y in range(1,int(b/2)+1):
        if b % y == 0:
            sum2 = sum2 + y


    if (sum2 == a) and (sum1 == b) and (a !=b) and (a<b):
        print(a)
        print(b)
        return a+b
    else:
        return 0
sum = 0
for i in range (1,10000):
    for j in range(1,10000):
        f = amicable(i,j)
        sum = sum +f
print(sum)
