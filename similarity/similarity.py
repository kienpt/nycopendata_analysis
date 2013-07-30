import sets

def preprocess(s):
	chars = ['-', '(', ')', ':', ',', '\n']	
	for c in chars:
		s.replace(c, '')
	s = s.lower()
	return s


stopwords = [	'',
		'and',
		'for',
		'null']	

f_meta = open('data/similarity_meta.csv','w')
f_schema = open('data/similarity_schema.csv','w')
f_combine = open('data/similarity.csv','w')
metadatas = []
schemes = []

ids = []
names = []
#Load metadata of each dataset into a set; all these sets are stored in metadatas
with open('../metadata/data/metadata.csv') as lines:
	for line in lines:
		_array = preprocess(line).split('\t')
		aSet = set()
		for i in range(1, len(_array)):
			words = _array[i].split()
			for word in words:
				if word not in stopwords:
	                		aSet.add(word)
		metadatas.append(aSet)	
		ids.append(_array[0])
		names.append(_array[1])

#Load schema of each dataset into a set; all these sets are stored in schemes
with open('../metadata/data/schema.csv') as lines:
        for line in lines:
                _array = preprocess(line).split('\t')
                aSet = set()
                for i in range(1, len(_array)):
                        words = _array[i].split()
                        for word in words:
				aSet.add(word)
                schemes.append(aSet)

#Compute similarity based on Jaccard formula
count = 0 
c = 1.5
norm = 1 + c*1
for i in range(0, len(metadatas)):
	count += 1
	if count%10 == 0:
		print count
	for j in range(i+1, len(metadatas)):
		#Compute similarity based on metadata
		its_meta = metadatas[i].intersection(metadatas[j])
		uni_meta = metadatas[i].union(metadatas[j])
		sim_meta = len(its_meta)/float(len(uni_meta))
		f_meta.write(str(sim_meta) + '\t' + ids[i] + '\t' + ids[j] + '\t' + names[i] + '\t' + names[j] + '\n')

		#Compute similarity based on schema
		its_schema = schemes[i].intersection(schemes[j])
                uni_schema = schemes[i].union(schemes[j])
		if len(uni_schema) > 0:
	                sim_schema = len(its_schema)/float(len(uni_schema))
		else:
			sim_schema = 0
                f_schema.write(str(sim_schema) + '\t' + ids[i] + '\t' + ids[j] + '\t' + names[i] + '\t' + names[j] + '\n')

		#Compute combined siimilarities
		if sim_schema == 0:
			sim_schema = sim_meta
		sim = (sim_meta + c*sim_schema)/norm
		f_combine.write(str(sim) + '\t' + ids[i] + '\t' + ids[j] + '\t' + names[i] + '\t' + names[j] + '\n')

	
f_meta.close()
f_schema.close()
f_combine.close()




