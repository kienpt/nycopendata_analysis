import sets

foo = open('data/mysimilarity.csv','w')
sets = []
ids = []
with open('data/lower_data.csv') as lines:
	for line in lines:
		words = line.split()
		aSet = set()
		for i in range(1, len(words)):
                	aSet.add(words[i])
		sets.append(aSet)	
		ids.append(words[0])

for i in range(0, len(sets)):
	for j in range(i+1, len(sets)):
		its = sets[i].intersection(sets[j])
		uni = sets[i].union(sets[j])
		sim = len(its)/float(len(uni))
		foo.write(ids[i] + ' ' + ids[j] + ' ' + str(sim))
		for w in its:
			foo.write(' ' + w)
		foo.write('\n')
	
foo.close()




