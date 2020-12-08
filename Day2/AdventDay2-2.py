fin = open('adventdata.in','r')
#extracting passwords
code = [x.strip().split(":") for x in fin]
#counts valid passwords
count = 0
for x in code:
	#text proscessing
	arr = x[0].split("-")
	minimum = int(arr[0])
	maximum = int(arr[1][0:arr[1].find(" ")])
	letter = arr[1][-1]
	#problem requires that the letter appears at either the maximum index OR minmum index but not both
	if(x[1][minimum] == letter and x[1][maximum] != letter):	
		count = count + 1
		print("VALID")
	elif(x[1][minimum] != letter and x[1][maximum] == letter):
		count = count+1

print(count)
