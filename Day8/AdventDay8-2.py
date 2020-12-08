fin = open('adventdata.in','r')
fin = open('adventdata.in','r')
instructions = [x.strip().split(' ') for x in fin]

accumulator = 0 
'''
made this part into a function because the question requires you to keep going through the instructions
until you find a replacement that will not end in a loop
Will return true if loop is terminated ( index out of range if so), false if an instruction is repeated twice
'''
def simulation():
	index = 0
	accumulator = 0
	indicesVisited = []
	repeat = False
	while repeat == False:

		try:
			cool = instructions[index]
		except:
			print(accumulator)
			return True

		if index in indicesVisited:
			repeat = True
			return(False)
			break

		indicesVisited.append(index)

		if instructions[index][0] == "acc":
			accumulator = accumulator + int(instructions[index][1])
			index = index+1 

		elif instructions[index][0] == "jmp":
			index = index + int(instructions[index][1])

		else: index = index + 1
'''
goes through every instruction. Changes the instruction and thensees if the loop will terminate.
If not, will return that instruction to what it was before, and modify the next instruction in line
'''
def findTerminatingVal():
	for instruction in instructions:
		if instruction[0] == "nop":
			instruction[0] = "jmp"
			if simulation() == True:
				return accumulator
			else:
				instruction[0] = "nop"

		elif instruction[0] == "jmp":
			instruction[0] = "nop"
			if simulation() == True:
				return accumulator
			else:
				instruction[0] = "jmp"

findTerminatingVal()




