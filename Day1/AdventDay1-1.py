fin = open('adventdata.in','r')
entries = [x.strip() for x in fin]
#Iterates through each entry, finding another entry that adds to 2020, if not mves to next entry
def findNum():
	for entry1 in entries:
		for entry2 in entries:
			if int(entry1)+int(entry2) == 2020:
				#question asks to multiply thw two that add up to 2020
				return(int(entry1)*int(entry2))

print(findNum())
