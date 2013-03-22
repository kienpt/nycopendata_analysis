import os
import sys

os.system('rm tempgraph.csv')

no = float(sys.argv[1])

f = open('forgraph.csv','r')
foo = open('tempgraph.csv','a')

for line in f:
	x = line
	words = x.split()
	xaxis = float(words[0])
	
	if xaxis >= no:
		foo.write(x)
	
f.close()
foo.close()

os.system('xgraph tempgraph.csv')



