sum = 0
for n in range(2,2000000) :
	checknotprime = False

	for i in range(2,int(n/2)) :

		if(n%i==0) :

			checknotprime = True
			break

	if (checknotprime == False) :
		sum = sum + n
print(sum)
