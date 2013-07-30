#!/usr/bin/python
import sys
import libgeocoding
import csv
from sets import Set

out = open('data/uniq_restaurant.csv', 'w')
ids = Set([])
with open('data/restaurant.csv') as csvfile:
	reader = csv.reader(csvfile)
	for row in reader:
		if row[0] not in ids:
			ids.add(row[0])	
			out.write('\t'.join(row) + '\n')

print 'Done Writing ' + str(len(ids)) + ' lines.'
out.close()
