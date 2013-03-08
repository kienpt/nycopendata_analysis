#!/usr/bin/python
# -*- coding: utf-8 -*-

import json
import urllib2
import codecs
import socket

#Get the number of datasets
urlhandle = urllib2.urlopen('http://nycopendata.socrata.com/api/views.json?count=True')
content = urlhandle.read()
js = json.loads(content)
count = js['count']

#Output
f = codecs.open('data.csv', 'w', 'utf-8')

#Get metadata of the all datasets
print 'Total: ' + str(count)
pages = count/200 + 1 #total number of pages
for i in range(1, pages+1):
	print 'Getting data from page ' + str(i) + ' ...'
	urlhandle = urllib2.urlopen("http://nycopendata.socrata.com/api/views.json?limit=200&page=" + str(i))
	content = urlhandle.read()
	js = json.loads(content)

	for j in range(0, len(js)):

		temp = js[j]['id']
		print temp

		urlstr = "http://data.cityofnewyork.us/resource/%s.json" %temp

		try:		
			urlholder = urllib2.urlopen(urlstr, timeout=20)

			x = urlholder.read()
			jjss = json.loads(x)

			tempstr = ' '
		
			if len(jjss) == 0:
				tempstr = 'No_Record'
		
			else:
				for key in jjss[0]:
					tempstr = tempstr + ' ' + key

		except urllib2.URLError, e:
			tempstr = 'Connection_failed'

		except socket.timeout:
			tempstr = 'Connection_failed'


		tagstr = ' '
		if js[j].has_key('tags'):
			for t in js[j]['tags']:
				tagstr = tagstr + ' ' + t

		line = js[j]['id'] + ' ' +\
			js[j]['name'] + ' ' +\
			tempstr + tagstr + '\n\n'

		
		#Write to file			
		f.write(line)


print 'Done'
f.close()
