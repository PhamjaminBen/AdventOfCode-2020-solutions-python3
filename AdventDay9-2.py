fin = open('adventdata.in','r')
numbers = [int(x.strip()) for x in fin]

preamble_length = 25
#list of numbers that satisfy the requirement
working_numbers = []
def findOulier():
	for x in range(preamble_length,len(numbers)):
		previous = numbers[x-preamble_length:x]
		for number in previous:
			for number2 in previous:
				if number+number2 == numbers[x]:
					working_numbers.append(numbers[x])

	for x in  range(preamble_length,len(numbers)):
		if numbers[x] not in working_numbers:
			return numbers[x]

invalid_number = findOulier()

def findContiguous():
	for x in range(len(numbers)):
		num1 = numbers[x]
		sum_array = [num1]
		for y in range(x+1,len(numbers)):
			sum_array.append(numbers[y])

			if sum(sum_array) == invalid_number:
				sum_array.sort()
				return sum_array[0]+sum_array[-1]
			elif sum(sum_array) >= invalid_number:
				break

print(findContiguous())

			







