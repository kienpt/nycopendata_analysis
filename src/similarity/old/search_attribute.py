import sys

search = str(sys.argv[1])

f = open('attriutes_compare.csv','r')

count = 0

for line in f:

	words = line.split()
	
	for i in range(1, len(words)):
		
		temp = words[i]

		z = temp.find(search)
		
		if temp == search:
			print words[0]
			count = count + 1
			break

		else:
			if z != -1:
				print words[0]
				count = count + 1
				break

print 'total number: '
print count
