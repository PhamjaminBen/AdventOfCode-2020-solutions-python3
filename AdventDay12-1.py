import math
fin = open('adventdata.in','r')
instructions = [x.strip() for x in fin]
#Names explain themselves
current_angle = 0
x_pos = 0
y_pos = 0
for instruction in instructions:
	command = instruction[0]
	amount = int(instruction[1:])
	#used cosine and sine because whichever way its facing, either the sin or cosine is zero, and it will end up moving forward
	if command == 'F':
		x_pos = x_pos + math.cos(current_angle)*amount
		y_pos = y_pos + math.sin(current_angle)*amount
	#converts to radians because math.cos and math.sin use radians as input
	elif command == 'L': current_angle = current_angle + math.radians(amount)
	elif command == 'R': current_angle = current_angle - math.radians(amount)
	elif command == 'N': y_pos = y_pos + amount
	elif command == 'S': y_pos = y_pos - amount
	elif command == 'E': x_pos = x_pos + amount
	elif command == 'W': x_pos = x_pos - amount
#computes manhattan difference
print(math.ceil(abs(x_pos)+abs(y_pos)))
