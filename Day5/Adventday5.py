fin = open('adventdata.in','r')
#puts all boarding ids into a list
code = [x.strip() for x in fin]
# used for part 1 to find the maximum boarding pass
maxID = 0
#list of ID's used for part 2
IDs = []

for x in code:
	#inital range of values, will change for each letter in the pass
	row = [0,127]
	#if its B, changes range of seats to upper half only, if not, will change range to lower half
	for y in range(7):
		diff = row[1] - row[0]

		if x[y] == 'B':
			row[0] = row[0] + diff//2+1
			print(row) 
			
		else:
			row[1] = row[1] - (diff//2+1)
			print(row)
	#by now bot values in the list should be the correct row number
	rowNum = row[1]
	
	#same thing as row but with a different range. R means take the upper half
	column = [0,7]
	for z in range(7,10):
		diff1 = column[1] - column[0]
		if x[z] == 'R':
			column[0] = column[0] +1 + diff1//2
		else:
			column[1] = column[1] - 1 - diff1//2
	columnnum = column[1]
	
	#formula used to calculate seat ID
	ID = rowNum*8 + columnnum
	if( ID > maxID):
		maxID = ID

	IDs.append(ID)
#sorts the list for part two in order to find if theres a missing seat
IDs.sort()
#finds the missing seat by finding a number that is missing its increment in the value next to it
for x in range(len(IDs)):
	if IDs[x] + 1 != IDs[x+1]:
		print(IDs[x]+1)
		break
print(maxID)


