fin = open('adventdata.in','r')
#reading the file and extracting each line, then separating into two parts before and after the colon
passwords = [x.strip().split(":") for x in fin]
#counts how many valid passwords
count = 0
for x in passwords:
	#splits into the two numbers and assigns them to minimum and maximum
	arr = x[0].split("-")
	minimum = int(arr[0])
	#since the maximum can be more than 1 digit, used .find(" ") to limit to the space
	maximum = int(arr[1][0:arr[1].find(" ")])
	#finding necessary letter
	letter = arr[1][-1]
	#finds only one of the values at index min/max are equal to the letter given, if so the password is valid and added to the count
	if(x[1][minimum] == letter and x[1][maximum] != letter):	
		count = count + 1
	elif(x[1][minimum] != letter and x[1][maximum] == letter):
		count = count+1

print(count)

