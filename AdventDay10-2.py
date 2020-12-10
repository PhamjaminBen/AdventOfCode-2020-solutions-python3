import itertools
fin = open('adventdata.in','r')
adapters = [int(x.strip()) for x in fin]
adapters.append(0)
adapters.sort()
adapters.append(adapters[-1]+3)

#finds all of the adapters that you can't remove
unremovables = []
for x in range(0,len(adapters)-1):
	if adapters[x+1] - adapters[x] == 3:
		unremovables.append(adapters[x])
		unremovables.append(adapters[x+1])
unremovables.append(0)
list(set(unremovables)).sort()

'''
a little bit of combinatorics here. But basically, there are only differences of one and three, and we can count combinations from there.
Heres an example from reddit that explains it well

0 [1 2 3] 4 7 10 [11 12 13] 14 17 [18 19 20] 21 24 27 [28 29 30] 31 34 37 [38] 39 42 [43 44] 45 48 51 [52] 53 56 57 60 [61 62] 63 66 [67 68 69] 70 73 [74] 75 78 [79 80 81] 82 85 [86 87] 88 91 94 95 98 [99] 100 103 [104 105] 106 109 112 [113 114 115] 116 119 122 [123 124 125] 126 129 [130 131 132] 133 136 139 [140 141 142] 143 146 147 150 [151 152] 153 156

7*7*7*7*2*4*2*4*7*2*7*4*2*4*7*7*7*7*4=4628074479616
Basicaly for sets of three consecutive removables, there are 7 ways to on/off them [abc,a,b,c,ab,bc,ac]
you cant omit all three because there would be a gap of larger and three and the chain wouldnt work
for sets of two consecutive removables, 4 ways to on off them [ab,a,b,none]
for one, 2 ways [a, none]
then you miltiply all these possibilities at the end to get the number
'''
possiblecount = 1
temporary_removables = 0
for adapter in adapters:
	if adapter not in unremovables:
		temporary_removables = temporary_removables + 1
	else:
		if temporary_removables == 3:
			possiblecount = possiblecount*7
		elif temporary_removables == 2:
			possiblecount = possiblecount*4
		elif temporary_removables == 1:
			possiblecount = possiblecount*2

		temporary_removables = 0

print(possiblecount)
			

