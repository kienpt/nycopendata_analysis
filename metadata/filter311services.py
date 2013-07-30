#!/usr/bin/python
import re
import sys

_input = 'data/metadata.csv'
all_output = open('311_datasets_all.csv', 'w')
updated_output = open('311_datasets_updated.csv', 'w')
old_output = open('311_datasets_old.csv', 'w')
error_output = open('error_lines.txt', 'w')
_pattern = re.compile('311 Service Requests')
updated_pattern = re.compile('automatically updated daily')
with open(_input) as f:
	for line in f:
		array = line.split('\t')
		if len(array) == 7:
			_id = array[0]
			_des = array[5]
			_match = re.search(_pattern, line)
			if _match:
				all_output.write(_id + '\t' + _des + '\n')
				updated_match = re.search(updated_pattern, line)
				if updated_match:
					updated_output.write(_id + '\t' + _des + '\n')
				else:
					old_output.write(_id + '\t' + _des + '\n')
		else:
			error_output.write(line)
all_output.close()
updated_output.close()
old_output.close()
