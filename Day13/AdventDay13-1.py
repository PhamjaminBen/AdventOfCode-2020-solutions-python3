fin = open('adventdata.in','r')
earliest_time = int(fin.readline())
buses = fin.readline().split(',')
#gets rid of empty buses
buses = [int(x) for x in buses if x != 'x']

first_bus = 0
#super large so first bus time can be set to the first value
first_bus_time = 1000000000000000
for bus in buses:
	#takes the smallest difference 
	different = earliest_time -  earliest_time%bus + bus
	if different < first_bus_time:
		first_bus_time = different
		first_bus = bus

#prints out 
print((first_bus_time- earliest_time)*first_bus)
