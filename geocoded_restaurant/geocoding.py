#!/usr/bin/python
import sys
import libgeocoding
import libutility
import csv

count = 0
succ = 0
fail = 0
out = open('data/uniq_geocoded_restaurant.csv', 'a')
out_fail = open('data/uniq_fail_restaurant.csv', 'a')
ids = libutility.loadID('data/uniq_geocoded_restaurant.csv', 0)
ids_fail = libutility.loadID('data/uniq_fail_restaurant.csv', 0)
print len(ids)
print len(ids_fail)
with open('data/uniq_restaurant.csv') as csvfile:
	reader = csv.reader(csvfile, delimiter='\t', quotechar=None)
	for row in reader:
		if count == 0:
			head = row
		else:
			if (row[0] not in ids) & (row[0] not in ids_fail):
				temp = row[4].strip()
				street = temp.split(' ')
				length = len(street)
				if street[length-2].isdigit():
					no = int(street[length-2])
					_type = street[length-1]
					l = len(_type)
					if (no - 1)%10 == 0:
						street = temp[:-l].strip() + 'st ' + _type
					elif (no - 2)%10 == 0:
	                                        street = temp[:-l].strip()  + 'nd ' + _type
					elif (no - 3)%10 == 0:
                	                        street = temp[:-l].strip()  + 'rd ' + _type
					else:
						street = temp[:-l].strip()  + 'th ' + _type
				else:
					street = temp
				coordinate = libgeocoding.geocode(row[3].strip(), street, row[5].strip())
				if len(coordinate) == 2:
					line = row[0] + '\t' + row[1] + '\t' + coordinate[0] + '\t' + coordinate[1] + '\n'
					out.write(line)
					succ += 1
					if succ%1000 == 0:
						print succ
				else:
					line = row[0] + '\t' + row[1] + '\t' + coordinate+ '\n'
					out_fail.write(line)
					fail += 1
		count += 1
		if count%1000==0:
			print count
out.close()
out_fail.close()
