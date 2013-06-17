
import sets


f = open('lower_data.csv','r')

foo = open('similarity.csv','w')

for line in f:
	temp = line
	words = temp.split()

	hmm = set()

	for i in range(1, len(words)):
		hmm.add(words[i])

	f1 = open('lower_data.csv','r')
	
	flag = 0

	for line1 in f1:
		temp1 = line1
		
		words1 = temp1.split()

		if words[0] == words1[0]:
			flag = 1

		if flag == 1:	

			hmm1 = set()

			for j in range(1, len(words1)):
				hmm1.add(words1[j])

			x1 = hmm.intersection(hmm1)
			y1 = len(x1)
			z1 = hmm.union(hmm1)
			w1 = len(z1)
	
			sim = y1/float(w1)

			foo.write(words[0] + ' ' + words1[0] + ' ')
			foo.write(str(sim) + ' ')
			
			for goo in x1:
				foo.write(str(goo) + ' ')		
		
			foo.write('\n')

	f1.close()
	print words[0]
	

f.close()
foo.close()




