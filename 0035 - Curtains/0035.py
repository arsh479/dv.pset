f = 0
while f == 0:
    print(end='\n')
    print(end='\n')
    print(end='\n')
    x = input()
    i =0
    while i < len(x)+1:

        z= len(x) - (len(x) - i) #how the position system for picking lettes from string and len(x) work differently, had to modify len(x) to fit the system of x[something:something]
        a = x[0:z]#to pick letters from a position to the other inside the input string
        print(a)
        i = i+1#to keep increasing the range of the strings values being printed afetr everytime loop runs
        continue
