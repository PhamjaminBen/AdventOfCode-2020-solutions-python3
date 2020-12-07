fin = open('adventdata.in','r')
#reading the file and extracting each line, then separating into two parts before and after the colon
passwords = [x.strip().split(":") for x in fin]
#counts how many valid passwords
count = 0
for x in passwords:
	#used to count how many times letter appears
	tempcount = 0
	#splits into the two numbers and assigns them to minimum and maximum
	arr = x[0].split("-")
	minimum = int(arr[0])
	#since the maximum can be more than 1 digit, used .find(" ") to limit to the space
	maximum = int(arr[1][0:arr[1].find(" ")])
	#finding necessary letter
	letter = arr[1][-1]
	# counts how many times a letter appearsin the password
	for y in x[1]:
		if y == letter: tempcount = tempcount+1

	#makes sure the amount of times letter is repeated is within the constraints, and adds to valid count
	if tempcount >= minimum and tempcount <= maximum: count = count+1

print(count)