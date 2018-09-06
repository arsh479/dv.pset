import random
i = 0
u = 0
while i == 0:
    x = int(input("Enter a digit: ")) #digit x sets range

    y = random.randint(1, x)#put in while loop so everytime different no. is generated
    while u ==0:
        z = int(input("Guess Number: "))

        if z>y: #conditions for high, low, equal
            print("high")


        elif y> z:
            print("low")


        elif y == z:
            print("correct")
            print("press ctrl + c to exit")


            break
