fin = open('adventdata.in','r')
entries = [x.strip() for x in fin]
#iterates through all possible pairs of three that add up to 2020 nand prints the product of those 3
def findNum():
	for entry1 in entries:
		for entry2 in entries:
			for entry3 in entries:
				if int(entry1)+int(entry2)+ int(entry3) == 2020:
					return(int(entry1)*int(entry2)*int(entry3))

print(findNum())

		