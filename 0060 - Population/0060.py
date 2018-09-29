a = 50*(10**6)
b = 70*(10**6)
i = 0
while i>=0:
    i = i+1
    a = int(a + (3/100)*a)
    b = int(b + (2/100)*b)

    if a>b:
        print(str(a)+ (' people in A'))
        print(str(b)+ (' people in B'))
        print(str(i)+str(' years'))
        break
