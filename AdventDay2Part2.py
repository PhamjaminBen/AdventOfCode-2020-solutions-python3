fin = open('adventdata.in','r')
code = [x.strip().split(":") for x in fin]
count = 0
for x in code:
	arr = x[0].split("-")
	minimum = int(arr[0])
	maximum = int(arr[1][0:arr[1].find(" ")])
	letter = arr[1][-1]
	print(f'{minimum}:{maximum}:{letter}:{x[1]}')
	if(x[1][minimum] == letter and x[1][maximum] != letter):	
		count = count + 1
		print("VALID")
	elif(x[1][minimum] != letter and x[1][maximum] == letter):
		count = count+1

print(count)

