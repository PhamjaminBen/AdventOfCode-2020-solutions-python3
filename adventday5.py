fin = open('adventdata.in','r')
code = [x.strip() for x in fin]
print(code)
maxID = 0
IDs = []
for x in code:
	row = [0,127]
	for y in range(7):
		diff = row[1] - row[0]

		if x[y] == 'B':
			row[0] = row[0] + diff//2+1
			print(row) 
			
		else:
			row[1] = row[1] - (diff//2+1)
			print(row)

	rowNum = row[1]

	column = [0,7]
	for z in range(7,10):
		diff1 = column[1] - column[0]
		if x[z] == 'R':
			column[0] = column[0] +1 + diff1//2
		else:
			column[1] = column[1] - 1 - diff1//2
		print(column)
	columnnum = column[1]

	ID = rowNum*8 + columnnum
	if( ID > maxID):
		maxID = ID

	IDs.append(ID)
	print(maxID)

IDs.sort()

for x in range(len(IDs)):
	if IDs[x] + 1 != IDs[x+1]:
		print(IDs[x]+1)
		break
print(IDs)


