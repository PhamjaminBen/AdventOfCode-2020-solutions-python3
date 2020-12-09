fin = open('adventdata.in','r')
#splits input data into separate passports
code = fin.read().split('\n\n')
#splits passports by each section
code = [x.split() for x in code]

#array of valid sections (that are required)
valids = ['byr','iyr','eyr','hgt','hcl','ecl','pid']
validCount = 0
#goes through each passport, making sure it is valid
for x in code:
	#counts how many section of passport are valid (if its in valids array)
	count = 0
	valid_fields = 0
	for y in x:
		field = y[0:3]
		if field in valids:
			valid_fields = valid_fields + 1
	#if passport contains all 7 fields, it will be valid
	if valid_fields == 7:
		validCount = validCount +1

print(validCount)
