#!/usr/bin/python
import json
import sys
import ijson

#the script not only convert from json but also filter the important attributes

def main(argv):
	_id = argv[0]
	_input = '../../datasets/data/json/' + _id
	_output = 'csv/' + _id +'.csv'
	print _output 
	_f = open(_input)
	_out = open(_output, 'w')
	_data = ijson.items(_f, 'data.item')
	count = 0
	for x in _data:
		#ID
		line =  str(x[0])
		#Complaint type
		line = line + '\t' + x[13] 
		#Longtitude
		if x[58] is None:
			continue
		line = line + '\t' + x[58]
		#Latitude
		line = line + '\t' + x[57]
		if x[57] is None:
			continue
		#CreatedTime
		line = line + '\t' + x[9]
		#ClosedTime
		if x[10] is None:
			ct = x[9]
		else:
			ct = x[10]
		line = line + '\t' + ct
		#Descriptor
		if x[14] is None:
			des = x[13]
		else:
			des = x[14]
		line = line + '\t' + des
		#AgencyName
		line = line + '\t' + x[12] + '\n'
		_out.write(line)
		count += 1
		if (count % 1000) == 0:
			print count
	_out.close()

if __name__ == "__main__":
	main(sys.argv[1:])

