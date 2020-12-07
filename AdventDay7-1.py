fin = open('adventdata.in','r')
rules = [x.strip() for x in fin]
refinedRule = {}
bags = []
for rule in rules:
	tempRule = [rule[0:rule.index(" bags")]]
	temp = rule[rule.index("contain")+8:].split(", ")
	for x in temp:
		tempRule.append(x[2:x.index(" bag")])
	bags.append(tempRule[0])
	refinedRule[tempRule[0]] = tempRule[1:]
print(bags)
print(refinedRule)

#iterate through all bags to get rules

def findbag(bag):
	if 'shiny gold' in refinedRule[bag]:
		print("found it")
		return(True)
	elif ' other' in refinedRule[bag]:
		print("nothing here.")
		return(False)
	else:
		return any([findbag(bag) for bag in refinedRule[bag]])

validBagCount = 0
for bag in bags:
	if(findbag(bag)) == True:
		validBagCount = validBagCount + 1

print(validBagCount)


