fin = open('adventdata.in','r')
rules = [x.strip() for x in fin]
refinedRule = {}
bags = []
#same as part 1, but includes the number of sub bags this time
for rule in rules:
	tempRule = [rule[0:rule.index(" bags")]]
	temp = rule[rule.index("contain")+8:].split(", ")
	for x in temp:
		tempRule.append(x[0:x.index(" bag")])
	bags.append(tempRule[0])
	refinedRule[tempRule[0]] = tempRule[1:]

#recursion in order to find how many bags a gold bag can hold
def findbag(bag):
	#if it reaches the end, then no more bags
	if 'no other' in refinedRule[bag]:
		return 0
	else:
		#counts how many bags basically
		bagcount = 0
		for subBag in refinedRule[bag]:
			#splits into number of bags and type of bags
			number = int(subBag[0])
			bagType = subBag[2:]
			#increments the bag count by the bag itself,and then the number of each type of bag THAT bag holds, kinda hard to explain
			bagcount = bagcount + number + number*findbag(bagType)

		return(bagcount)

print(findbag('shiny gold'))
