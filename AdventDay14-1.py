fin = open('adventdata.in','r')
raw_data = [x.strip() for x in fin]
#dictionary since each memory can only hold one value
memory = {}

current_mask = ""
for command in raw_data:

	if command[:4] == 'mask':
		current_mask = list(command[7:])
		continue

	else:
		slot = int(command[4: command.index(']')])
		value_raw = command[command.index('=')+2:]
		#converts into a list of binary digits, fills to 36 values because the mask could overwrite the leading zeroes
		value_bin = list(bin(int(value_raw))[2:].zfill(36))
		#python lists can be referenced negatively so we can go backwards
		index = -1
		while True:
			#makes sure it doesnt go more negative than one list so it goes through values once
			if abs(index) > len(value_bin):
				break
			if current_mask[index] != 'X':
				value_bin[index] = current_mask[index]

			index = index - 1
		#COMBINES binary into string the processes it into an integer
		value_bin = "".join(value_bin)
		memory[slot] = int(value_bin,2)

final_sum = 0
#adds up all memory values
for memo in memory:
	final_sum = final_sum + memory[memo]

print(final_sum)



