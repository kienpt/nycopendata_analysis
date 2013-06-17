#!/usr/bin/python
# -*- coding: utf-8 -*-

import json
import urllib
import codecs
import sys

def loadIDs():
	#Input
	filepath = 'data/metadata.csv'
	
	ids = set([])
	with open(filepath) as f:
		for line in f:
			_array = line.split('\t')
			ids.add(_array[0])
	print 'Done loading IDs'
	return ids

def main(argv):
	#Get the number of datasets
	urlhandle = urllib.urlopen('http://nycopendata.socrata.com/api/views.json?count=True')
	content = urlhandle.read()
	js = json.loads(content)
	count = js['count']

	#Output
	meta_f = codecs.open('data/metadata.csv', 'a', 'utf-8')
	tag_f = codecs.open('data/tags.csv', 'a', 'utf-8')
	schema_f = codecs.open('data/schema.csv', 'a', 'utf-8')
	
	#Load id of the datasets whose metadatas were already retrieved
	ids = loadIDs()

	#Get metadata of the all datasets
	#Metadata for one dataset is formated in one line. Each attribute value is seperated by tab character and empty value is replaced by the string 'Null'
	print 'Total: ' + str(count)
	pages = count/200 + 1 #total number of pages
	
	for i in range(1, pages+1):
		sys.stdout.write('Getting data from page ' + str(i) + ' ... ')
		urlhandle = urllib.urlopen("http://nycopendata.socrata.com/api/views.json?limit=200&page=" + str(i))

		content = urlhandle.read()
		js = json.loads(content)
		for j in range(0, len(js)):
			#Check whether the metadata was already retrieved
			_id = js[j]['id']
			if _id in ids:
				continue
				
			#Get metadata of each dataset
			#ID and NAME
			meta = js[j]['id'] + '\t' + js[j]['name']
			
			#DESCRIPTION
			if js[j].has_key('description'):
				meata = meta + '\t' + js[j]['description'].replace('\n', ' ')
			else:
				meta = meta + '\t' + 'null'

			#TAGS
			tag  = ''
			if js[j].has_key('tags'):
				for t in js[j]['tags']:
					tag_f.write(t + '\n')
					tag = tag + ' ' + t
				meta = meta + '\t' + tag + '\n'
			else:
				meta = meta + '\t' + 'null\n'
			meta_f.write(meta)
		
			#Get schema of each dataset
			url = "http://nycopendata.socrata.com/api/views/" + js[j]['id'] + '.json'
			aJS = json.loads(urllib.urlopen(url).read())
			if aJS.has_key('columns'):
				print url
				schema_js = aJS['columns']
				schema = js[j]['id']
				for field in schema_js:
					schema = schema + '\t' + field['fieldName']
				schema_f.write(schema + '\n')
			else:
				print js[j]['id']
			
		print 'Done'
	print 'Done'
	meta_f.close()
	tag_f.close()
	schema_f.close()

if __name__ == "__main__":
	main(sys.argv[1:])
