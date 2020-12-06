fin = open('adventdata.in','r')
#splits into groups
groups = fin.read().split('\n\n')
#splits groups into separate people
groups = [x.split('\n') for x in groups]
#counts aggregate number of questions answered yes by every person each group
answerCount = 0

for group in groups:
	'''
	dictionary of answers: 
	Key is the answer and value is the number of times that has been answered in the group
	'''
	answers = {}
	for person in group:
		for answer in person:
			#if the answer is in the dictionary you add one to its count, else you make it a new dictionary key
			if answer in answers:
				answers[answer] = answers[answer] +1
			else:
				answers[answer] = 1
	'''
	checks by comparing the amount of people in the group to the number of time that question has been answered yes.
	If they are equal (everyone in the group answered yes), adds one to the answer count
	'''
	for letter in answers:
		if answers[letter] == len(group):
			answerCount = answerCount + 1

print(answerCount)