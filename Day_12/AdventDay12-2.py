import math
fin = open('adventdata.in','r')
instructions = [x.strip() for x in fin]
#coordinates for both car and waypoint
car_x_pos = 0
car_y_pos = 0
waypoint_x_pos = 10
waypoint_y_pos = 1
for instruction in instructions:
	command = instruction[0]
	amount = int(instruction[1:])
	#used for calculating the rotation
	x_diff = (waypoint_x_pos - car_x_pos)
	y_diff = (waypoint_y_pos - car_y_pos)
	#moving forward is based on the difference btwn car and waypoint
	if command == 'F':
		x_change =  (waypoint_x_pos - car_x_pos)*amount
		y_change =(waypoint_y_pos - car_y_pos)*amount
		waypoint_x_pos = waypoint_x_pos + x_change
		waypoint_y_pos = waypoint_y_pos + y_change
		car_x_pos = car_x_pos + x_change
		car_y_pos = car_y_pos + y_change
	elif command == 'L': 
		'''
		for rotations (clockwise) (x,y), 90 degrees = -y,x, 180 degrees = (-x,-y) and 270 degrees = (y,-x)
		counterclockwise, 90 and 270 degrees are switched
		'''
		if amount == 90: 
			waypoint_x_pos = car_x_pos + -1*y_diff
			waypoint_y_pos = car_y_pos + x_diff
		if amount == 180:
			waypoint_x_pos = car_x_pos + -1*x_diff
			waypoint_y_pos = car_y_pos + -1*y_diff
		if amount == 270:
			temp = waypoint_x_pos
			waypoint_x_pos = car_x_pos + y_diff
			waypoint_y_pos = car_y_pos + -1*x_diff
	elif command == 'R': 
		if amount == 270: 
			waypoint_x_pos = car_x_pos + -1*y_diff
			waypoint_y_pos = car_y_pos + x_diff
		if amount == 180:
			waypoint_x_pos = car_x_pos + -1*x_diff
			waypoint_y_pos = car_y_pos + -1*y_diff
		if amount == 90:
			temp = waypoint_x_pos
			waypoint_x_pos = car_x_pos + y_diff
			waypoint_y_pos = car_y_pos + -1*x_diff
	elif command == 'N': waypoint_y_pos = waypoint_y_pos + amount
	elif command == 'S': waypoint_y_pos = waypoint_y_pos - amount
	elif command == 'E': waypoint_x_pos = waypoint_x_pos + amount
	elif command == 'W': waypoint_x_pos = waypoint_x_pos - amount

#calculates manhattan distance
print(abs(car_x_pos)+abs(car_y_pos))
