
import sets

f = open('set_data.csv','r')

foo = open('hope.csv','a')

for line in f:
	temp = line
	words = temp.split()

	hmm = set()

	for word in words:
		hmm.add(word)

	f1 = open('set_data.csv','r')
	
	flag = 0

	for line1 in f1:
		temp1 = line1
		
		words1 = temp1.split()

		if words[0] == words1[0]:
			flag = 1

		if flag == 1:
					

			hmm1 = set()

			for word1 in words1:
				hmm1.add(word1)

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

	

f.close()
foo.close()




