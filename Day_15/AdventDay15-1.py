fin = open('adventdata.in','r')
starting_nums = fin.readline().split(",")
starting_nums = [int(x) for x in starting_nums]
#dictionary used for keeping the last time the number was said
numbers_last_dict = {}
for turn in range(1,len(starting_nums)+1):
	number = starting_nums[turn-1]
	numbers_last_dict[number] = turn

#removes the last number in the dict because the prompt asks to analyze the last number spoken
#therefore, we update the dictionary after determining if it had been spoken before
del numbers_last_dict[starting_nums[-1]]
last_spoken = starting_nums[-1]

for turn in range(len(starting_nums)+1,2021):
	#determines if the last number had been spoken before, if so finds the difference and makes that the new num
	#if not then it will make the new num 0 (not spoken before) and set the number in the dictionary
	if last_spoken in numbers_last_dict:
		diff = turn - numbers_last_dict[last_spoken] -1
		numbers_last_dict[last_spoken] = turn-1
		last_spoken = diff
	else:
		numbers_last_dict[last_spoken] = turn-1
		last_spoken = 0	

print(last_spoken)