fin = open('adventdata.in','r')
#splits into groups
groups = fin.read().split('\n\n')
#split those groups into people (gets rid of newlines also)
groups = [x.split('\n') for x in groups]
#since we dont need to know answer per person, we can just combine all the answers
groups = ["".join(x) for x in groups]
#counts aggregate number of unique answers per group
answerCount = 0

#for each group an array will store the answers that each person gives
for group in groups:
	answers = []
	for answer in group:
		answers.append(answer)
	#adds the amount of unique answers per group to the aggregate count
	answerCount = answerCount + len(set(answers))

print(answerCount)
