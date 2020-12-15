import itertools
fin = open('adventdata.in','r')

raw_data = [x.strip() for x in fin]
memory = {}

current_mask = ""
for command in raw_data:

	if command[:4] == 'mask':
		current_mask = list(command[7:])
		#list of where the floating values (either 1 or 0 marked by an X) are 
		replacements = []
		for x in range(len(current_mask)):
			if current_mask[x] == 'X':
				replacements.append(x)
		continue

	else:
		slot = int(command[4: command.index(']')])
		slot_bin = list(bin(int(slot))[2:].zfill(36))
		value_raw = command[command.index('=')+2:]
		value_bin = list(bin(int(value_raw))[2:].zfill(36))
		index = -1
		while True:
			if abs(index) > len(value_bin):
				break
			#only digits of 1 in the mask will overwrite the slot
			if current_mask[index] == '1':
				slot_bin[index] = current_mask[index]
			index = index - 1

		value_bin = "".join(value_bin)

		#finds every possible combination of 1 and 0 for the floating values using itertools
		for length in range(0,len(replacements)+1):
			for combo in itertools.combinations(replacements,length):
				for replacement_index in replacements:
					if replacement_index in combo: 
						slot_bin[replacement_index] = '1'
					else: 
						slot_bin[replacement_index] = '0'

				newslot = int("".join([str(x) for x in slot_bin]),2)
				memory[newslot] = int(value_bin,2)


final_sum = 0
for memo in memory: 
	final_sum = final_sum + memory[memo]

print(final_sum)



