#Separate the big 311 datasets into complaint type based ones
import sys

m = {}
with open("erm2-nwe9.json.count.sorted") as f:
	for line in f:
		a = line.split("\t")
		_type = a[0].replace("/", "-").replace(" ", "_")
		m[_type] = open("erm2-nwe9/" + _type + ".csv", 'w')

with open("../../json2csv/311/csv/erm2-nwe9.json.csv") as f:
	for line in f:
		a = line.split("\t")
		_type = a[1].replace("/", "-").replace(" ", "_")
		m[_type].write(line)

for key in m.keys():
	m[key].close()

