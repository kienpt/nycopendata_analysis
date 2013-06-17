from sets import Set

schema = "../metadata/data/schema.csv"
cluster = "../cluster/data/clusters_id.csv"
output = open("data/attributeDist_u.csv", "w")


m = {} #Map attribute name to number of its occurance 
id2c = {} #Map id to its corresponding schema

with open(schema) as f:
	for line in f:
		_array = line.strip('\n').split('\t', 1)
		if len(_array) == 2:
			id2c[_array[0]] = _array[1]
with open(cluster) as f:
	for line in f:
		#For each cluster
		s = Set([]) # s contains the set of unique attributes in the cluster
		ids = line.strip('\n').split('\t')
		for i in range(1, len(ids)):
			if id2c.has_key(ids[i]):
				attributes = id2c[ids[i]].split('\t')
				for a in attributes:
					s.add(a)
		for _id in s:
			if m.has_key(_id):
				m[_id] += 1
			else:
				m[_id] = 1

for key in m.keys():
	output.write(key + '\t' + str(m[key]) + '\n')
