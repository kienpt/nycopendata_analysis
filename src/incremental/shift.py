
f = open('attributes.csv','r')
foo = open('attributes_norecords.csv','a')
loo = open('attributes_failed.csv','a')
zoo = open('attriutes_compare.csv','a')

for line in f:
	x = line
	words = x.split()
	
	#put records containg the word in one file and records not containing the word in another file
	
	flag = 0

	for word in words:
			
		if word == 'No_Record':
			foo.write(x)
			flag = 1

		if word == 'Connection_failed':
			loo.write(x)
			flag = 1
	
	if flag == 0:
		zoo.write(x)
			

f.close()
foo.close()
zoo.close()	
loo.close()	
