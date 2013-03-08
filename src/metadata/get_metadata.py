#!/usr/bin/python
# -*- coding: utf-8 -*-

import json
import urllib
import codecs

#Get the number of datasets
urlhandle = urllib.urlopen('http://nycopendata.socrata.com/api/views.json?count=True')
content = urlhandle.read()
js = json.loads(content)
count = js['count']

#Output
f = codecs.open('metadata.csv', 'w', 'utf-8')
tag_f = codecs.open('tags.csv', 'w', 'utf-8')

#Get metadata of the all datasets
print 'Total: ' + str(count)
pages = count/200 + 1 #total number of pages
for i in range(1, pages+1):
	print 'Getting data from page ' + str(i) + ' ...'
	urlhandle = urllib.urlopen("http://nycopendata.socrata.com/api/views.json?limit=200&page=" + str(i))
	content = urlhandle.read()
	js = json.loads(content)
	for j in range(0, len(js)):
		line = js[j]['id'] + '\t' +\
			js[j]['name'] + '\t' +\
			str(js[j]['numberOfComments']) + '\t' +\
			str(js[j]['viewCount']) + '\t' +\
			str(js[j]['viewLastModified'])

		#Some of dataset does not contain the below attributes so we need to check first
		if js[j].has_key('description'):
			line = line + '\t' + js[j]['description']
		else:
			line = line + '\t' + 'null'

		if js[j].has_key('publicationDate'):
			line = line + '\t' + str(js[j]['publicationDate'])
		else:
			line = line + '\t' + 'null'
		#Write to file			
		f.write(line)

		#Write tags for another purpose
		if js[j].has_key('tags'):
			for t in js[j]['tags']:
				tag_f.write(t + '\n')
print 'Done'
f.close()
