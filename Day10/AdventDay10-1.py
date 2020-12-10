fin = open('adventdata.in','r')
adapters = [int(x.strip()) for x in fin]
#appends 0 for the original outlet and sorts from min to max
adapters.append(0)
adapters.sort()

onecount = 0
#starts with 1 because of the final adapter is always 3
threecount = 1
#simple linear seach. Finds differences of three and one 
for x in range(len(adapters)-1):
	diff = adapters[x+1] - adapters[x]
	if diff == 3: threecount = threecount+1
	elif diff == 1: onecount = onecount+1
#equation used to find answer
print(onecount*threecount)
