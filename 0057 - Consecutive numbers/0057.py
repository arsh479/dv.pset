x = int(input('Enter a digit: '))

f = 0
for i in range(1,x+1):
    for j in range(1,i+1):
        f = f+1
        print(f,end='')
    print(end='\n') #took a lot of help for this question, very little of my own contribution. but now i understand roughly how to do these kinda questions
