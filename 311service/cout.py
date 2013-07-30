#input: csv file (311)
import sys

m = {}
with open(sys.argv[1]) as f:
	for line in f:
		a = line.split('\t')
		complaint = a[1]
		if m.has_key(complaint):
			m[complaint] += 1
		else:
			m[complaint] = 1
for key in m.keys():
	print key + '\t' + str(m[key])
		


