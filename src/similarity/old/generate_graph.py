import os
import sys

os.system('rm data/tempgraph.csv')

no = float(sys.argv[1])

f = open('data/forgraph.csv','r')
foo = open('data/tempgraph.csv','a')

for line in f:
	x = line
	words = x.split()
	xaxis = float(words[0])
	
	if xaxis >= no:
		foo.write(x)
	
f.close()
foo.close()

os.system('xgraph data/tempgraph.csv')



