
fin = open('adventdata.in','r')
code = [x.strip().split(":") for x in fin]
print(code)
count = 0
for x in code:
	arr = x[0].split("-")
	print(arr)
	tempcount = 0
	min = int(arr[0])
	max = int(arr[1][0:arr[1].find(" ")])
	letter = arr[1][-1]
	print(f'max:{max},min{min}, letter:{letter}')
	for y in x[1]:
		if y == letter:
			tempcount = tempcount +1

	if tempcount >= min and tempcount <= max:
		count = count + 1

print(count)

