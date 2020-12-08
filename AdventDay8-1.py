fin = open('adventdata.in','r')
#splits input intoseparate instructions
instructions = [x.strip().split(' ') for x in fin]

index = 0 
accumulator = 0
#keeps track of indices visited so it detects when a instruction is repeated
indicesVisited = []
repeat = False
while repeat == False:
	#checks if instruction is repeated and terminates loop, if not adds the instruction to the array of visited indices
	if index in indicesVisited:
		repeat = True
		break
	indicesVisited.append(index)

	#checks the purpose of each instruction and applies it, then increments the index (unless its jmp)
	if instructions[index][0] == "acc":
		accumulator = accumulator + int(instructions[index][1])
		index = index+1 

	elif instructions[index][0] == "jmp":
		index = index + int(instructions[index][1])

	else: index = index + 1

print(accumulator)



