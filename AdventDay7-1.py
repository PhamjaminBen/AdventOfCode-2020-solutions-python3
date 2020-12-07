fin = open('adventdata.in','r')
rules = [x.strip() for x in fin]
#this will be a dictionary where the main bag will be the key and value will be the sub bags
refinedRule = {}
#list of bags
bags = []
#text proscessing 
for rule in rules:
	#finds main bag
	tempRule = [rule[0:rule.index(" bags")]]
	#finds the rest of the sub bag it contains (no need for numbers)
	temp = rule[rule.index("contain")+8:].split(", ")
	#really messy here, but basically makes a new dictionary slot for the bag
	for x in temp:
		tempRule.append(x[2:x.index(" bag")])
	bags.append(tempRule[0])
	refinedRule[tempRule[0]] = tempRule[1:]

#recursive function for finding if bag has gold
def findbag(bag):
	if 'shiny gold' in refinedRule[bag]:
		return(True)
	elif ' other' in refinedRule[bag]:
		return(False)
	else:
		#if any of the paths of the sub bags end up in gold, adds one to bag count
		return any([findbag(bag) for bag in refinedRule[bag]])

validBagCount = 0
for bag in bags:
	if(findbag(bag)) == True:
		validBagCount = validBagCount + 1

print(validBagCount)


