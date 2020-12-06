fin = open('adventdata.in','r')
code = [x.strip()*100 for x in fin]

def plane(x,y):
	x_pos = 0
	y_pos = 0
	x_change = x
	y_change = y
	count = 0
	print(code)
	print(len(code))
	while y_pos < len(code):
		print(f'y:{y_pos},x:{x_pos}')
		print(code[y_pos][x_pos])
		if code[y_pos][x_pos] == '#':
			count = count + 1
		y_pos = y_pos + y_change
		x_pos = x_pos + x_change
	return(count)

print(plane(1,1)*plane(3,1)*plane(5,1)*plane(7,1)*plane(1,2))

