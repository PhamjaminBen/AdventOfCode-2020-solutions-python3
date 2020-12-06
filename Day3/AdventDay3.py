fin = open('adventdata.in','r')
#scans the map and makes a 3d list of the map. Multiplied by 100 because the map is repeating itself horizontally.
code = [x.strip()*100 for x in fin]

#function for determining how many times the plane will hit a tree. X and Y determine change in plane's position every cycle
def plane(x,y):
	x_pos = 0
	y_pos = 0
	x_change = x
	y_change = y
	#counts num of trees hit
	count = 0
	while y_pos < len(code):
		#checks if a tree is at a plane's position. If so, then it adds it to the number of trees hit
		if code[y_pos][x_pos] == '#':
			count = count + 1
		y_pos = y_pos + y_change
		x_pos = x_pos + x_change
	return(count)
#calculation done for part 2
print(plane(1,1)*plane(3,1)*plane(5,1)*plane(7,1)*plane(1,2))

