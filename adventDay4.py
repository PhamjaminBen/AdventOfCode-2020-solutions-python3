fin = open('adventdata.in','r')
print(fin)
code = fin.read().split('\n\n')
code = [x.split() for x in code]

valid = ['byr','iyr','eyr','hgt','hcl','ecl','pid']
validCount = 0
for x in code:
	count = 0
	for y in x:
		field = y[0:3]
		value = y[4:]
		print(f'field:{field} Value:{value}')

		if field == 'byr' and int(value) >= 1920 and int(value) <= 2002:
			count = count+1

		elif field == 'iyr' and int(value) >= 2010 and int(value) <= 2020:
			count = count+1

		elif field == 'eyr' and int(value) >= 2020 and int(value) <= 2030:
			count = count+1

		elif field == 'hgt':
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
			else:
				print('invalid')


		elif field == 'hcl':
			if value[0] == '#' and len(value[1:]) == 6:
				acceptable = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']
				isGood = True
				for part in range(1,7):
					if value[part]  in acceptable:
						print(f'valid: {value[part]}')
					else:
						print(f'invalid: {value[part]}')
						isGood = False

				if isGood == True:
					count = count +1

		elif field == 'ecl':
			acceptable = ['amb','blu','brn','gry','grn','hzl','oth']
			if value in acceptable:
				count = count+1
			else:
				print(f'invalid: {value}')

		elif field == 'pid' and len(value) == 9 and value.isnumeric() :
			count = count+1
			print("valid")



	if count == 7:
		print('valid')
		validCount = validCount+1


print(validCount)
