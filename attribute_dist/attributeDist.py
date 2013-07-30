inputfile = "../metadata/data/schema.csv"
output = open("data/attributeDist.csv", "w")


m = {} #Map attribute name to number of its occurance 
with open(inputfile) as f:
	for line in f:
		_array = line.strip('\n').split("\t")
		for i in range(1, len(_array)):
			if m.has_key(_array[i]):
				m[_array[i]] += 1
			else:
				m[_array[i]] = 1

for key in m.keys():
	output.write(key + '\t' + str(m[key]) + '\n')
