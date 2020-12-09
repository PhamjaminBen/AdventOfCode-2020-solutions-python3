fin = open('adventdata.in','r')
numbers = [int(x.strip()) for x in fin]

preamble_length = 25
#list of numbers that satisfy the requirement
working_numbers = []
#iterates through all numbers
def findOulier():
	for x in range(preamble_length,len(numbers)):
		#array of previous numbers used to add together
		previous = numbers[x-preamble_length:x]
		#goes through all possible combination of numbers
		for number in previous:
			for number2 in previous:
				#if the number satisfies requirement its added to the working numbers
				if number+number2 == numbers[x]:
					working_numbers.append(numbers[x])
	#checks for the first number that fails and returns it
	for x in  range(preamble_length,len(numbers)):
		if numbers[x] not in working_numbers:
			return numbers[x]
					
print(findOulier())
