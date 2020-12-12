fin = open('adventdata.in','r')
seats = [list(x.strip()) for x in fin]

previous_final_taken = 0
while True:
	#arrays detailing which seats should be replaced by hashtags or Ls
	replacement_hashtag = []
	replacement_L = []
	for y in range(len(seats)):
		for x in range(len(seats[0])):
			seat = seats[y][x]
			#array of the positions of seats adjacent to the current seat
			adjacents = [[y+1,x],[y-1,x],[y,x+1],[y,x-1],[y+1,x+1],[y-1,x+1], [y+1,x-1],[y-1,x-1]]
			if seat == 'L':
				anytaken = False
				for adjacent_seat in adjacents:
					#if below zero, then it will wrap around the array which we do not want
					if adjacent_seat[0] >= 0 and adjacent_seat[1] >= 0:
						y_co = adjacent_seat[0]
						x_co = adjacent_seat[1]
					else:
						#if its below zero we just set it to a large index so it will get an error
						x_co = 1000
						y_co = 1000
					try:
						#makes sure that it is in the range of the array, if not then skips the adjacent seat
						seats[y_co][x_co]
					except:
						pass
					else:
						#checks if any seats around it are taken
						if seats[y_co][x_co] == '#':
							anytaken = True

				if anytaken == False:
					replacement_hashtag.append([y,x])
					

			elif seat == '#':
				#coutns number of seats around to see if it meets threshold
				taken_count = 0
				for adjacent_seat in adjacents:
					if adjacent_seat[0] >= 0 and adjacent_seat[1] >= 0:
						y_co = adjacent_seat[0]
						x_co = adjacent_seat[1]
					else:
						x_co = 1000
						y_co = 1000
					try:
						seats[y_co][x_co]
					except:
						#print("didn't work")
						pass
					else:
						if seats[y_co][x_co] == '#':
							taken_count = taken_count + 1
				#print(taken_count)
				if taken_count > 3:
					replacement_L.append([y,x])

	#this is where the replacement arrays come into play
	for y,x in replacement_hashtag:
		seats[y][x] = '#'

	for y,x in replacement_L:
		seats[y][x] = 'L'


	final_taken = 0
	for row in seats:
		for seat in row:
			if seat == "#":
				final_taken = final_taken + 1

	#IF final taken doesnt change means that it is finished so breaks the loop and prints the final count of taken seats
	if final_taken == previous_final_taken:
		break
	else:
		previous_final_taken = final_taken

print(final_taken)

