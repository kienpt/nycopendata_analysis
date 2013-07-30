#!/usr/bin/python
import sys
from sets import Set

def loadID(filename, index):
#index starts at 0
	ids = Set([])
	with open(filename) as f:
		for line in f:
			_id = line.strip().split('\t')[index]
			ids.add(_id)
	return ids

def main(argv):
	filename = argv[0]
	ids = loadID(filename, 1)
	print "Number of unique ids: " + str(len(ids))

if __name__ == '__main__':
	main(sys.argv[1:])
