#!/usr/bin/python
#Input format: id1 id2 score
import sets
import sys

sim_f = "../similarity/data/similarity.csv"
id_f = "../metadata/data/metadata.csv" 
cluster_id = open("data/clusters_id.csv", 'w') #Each line contains one cluster
cluster_name = open("data/clusters_name.csv", 'w')
cluster_size = open("data/clusters_size.csv", 'w')

def main(argv):
	t = argv[0] #Threashold 
	id2c = {} #Map an id to its cluster
	id2n = {} #Map an id to its name
	#Initialize id2c and id2n
	with open(id_f) as f:
		for line in f:
			_array = line.strip("\n").split("\t")
			_id = _array[0]
			cluster = set([_id])
			id2c[_id] = cluster
			id2n[_id] = _array[1]
	#clustering
	with open(sim_f) as f:
		for line in f:
			_array = line.split("\t")
			score = _array[0]
			if score >= t:	
				id1 = _array[1]
				id2 = _array[2]
				#merge two clusters
				for _id in id2c[id1]:
					id2c[id2].add(_id)
				for _id in id2c[id2]:
					id2c[_id] = id2c[id2]
	#output clusters
	buff = set([]) #Use this to store considered ids to avoid duplication
	s = 0
	for key in id2c.keys():
		if key not in id2c[key]:
			print 'Error'
		if key not in buff:
			ids = ''
			names = ''
			for _id in id2c[key]:
				buff.add(_id)
				ids = ids + '\t' + _id
				names = names + '\t' + id2n[_id]
			ids.strip('\t')
			names.strip('\t')
			cluster_id.write(str(len(id2c[key])) + '\t' + ids + '\n')
			cluster_name.write(str(len(id2c[key])) + '\t' + names + '\n')
			cluster_size.write(str(len(id2c[key])) + '\n')
			s += len(id2c[key])
	print s
	print len(buff)
	cluster_id.close()
	cluster_name.close()
	cluster_size.close()
			
if __name__ == "__main__":
	main(sys.argv[1:])
