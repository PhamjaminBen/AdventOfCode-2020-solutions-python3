fin = open('adventdata.in','r')
starting_nums = fin.readline().split(",")
starting_nums = [int(x) for x in starting_nums]
numbers_last_dict = {}
for turn in range(1,len(starting_nums)+1):
	number = starting_nums[turn-1]
	numbers_last_dict[number] = turn

del numbers_last_dict[starting_nums[-1]]
last_spoken = starting_nums[-1]

#literally the same as last time but it will take ~20-30 seconds to run since the larger amt of turns
for turn in range(len(starting_nums)+1,30000001):

	if last_spoken in numbers_last_dict:
		diff = turn - numbers_last_dict[last_spoken] -1
		numbers_last_dict[last_spoken] = turn-1
		last_spoken = diff
	else:
		numbers_last_dict[last_spoken] = turn-1
		last_spoken = 0	

print(last_spoken)