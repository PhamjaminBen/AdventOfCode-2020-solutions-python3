fin = open('adventdata.in','r')
#splits input data into separate passports
code = fin.read().split('\n\n')
#splits passports by each section
code = [x.split() for x in code]

validCount = 0
#goes through each passport, making sure it is valid
for x in code:
	#counts how many section of passport are valid
	count = 0
	for y in x:
		#assigning the field and value makign it easier to use in if/then statement
		field = y[0:3]
		value = y[4:]
		
		
		#series of tests for each section in the passport. If a value is valid for a field, the count is added
		if field == 'byr' and int(value) >= 1920 and int(value) <= 2002:
			count = count+1

		elif field == 'iyr' and int(value) >= 2010 and int(value) <= 2020:
			count = count+1

		elif field == 'eyr' and int(value) >= 2020 and int(value) <= 2030:
			count = count+1

		elif field == 'hgt':
			#in case there are no units/amount given, voids the units so no points will be added
			try:
				int(value[0:-2])
			except:
				unit = ' '
			else:
				amt = int(value[0:-2])
			unit = value[-2:]
			if unit == 'cm' and amt >= 150 and amt <= 193:
				count = count +1
			elif unit == 'in' and amt >= 59 and amt <= 76:
				count = count+1


		elif field == 'hcl':
			if value[0] == '#' and len(value[1:]) == 6:
				#acceptable values for the next 6 numbers in this list
				acceptable = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']
				isGood = True
				for part in range(1,7):
					if value[part]  in acceptable:
						pass
					else:
						isGood = False
				if isGood == True:
					count = count +1

		elif field == 'ecl':
			#acceptable eye color values
			acceptable = ['amb','blu','brn','gry','grn','hzl','oth']
			if value in acceptable:
				count = count+1

		elif field == 'pid' and len(value) == 9 and value.isnumeric() :
			count = count+1


	#if all 7 fields are valid (no cid since its optional) then the passport is deemed valid and added to the valid passport count
	if count == 7:
		print('valid')
		validCount = validCount+1


print(validCount)
