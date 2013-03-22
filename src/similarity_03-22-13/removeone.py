
f = open('similar123.csv','r')
foo = open('imp_similarity.csv','a')

for line in f:
	x = line

	words = x.split()

	temp = words[2]
	z =float(temp)
	
	if z < 1 and z > 0.1:
		foo.write(x)
	
				

	

#print count	
f.close()
foo.close()
