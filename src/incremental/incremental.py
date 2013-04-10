
import sets
import json
import urllib2
import codecs
import socket
import string


f = open('data_compare.csv','r')
foo = open('data_norecords.csv','r')
hmm = set()

for line in f:
	words = line.split()
	hmm.add(words[0])

f.close()

for line in foo:
	words = line.split()
	hmm.add(words[0])

foo.close()

print len(hmm)

new_count = 0

#Get the number of datasets
urlhandle = urllib2.urlopen('http://nycopendata.socrata.com/api/views.json?count=True')
content = urlhandle.read()
js = json.loads(content)
count = js['count']

#Output
f = codecs.open('incremental_newdata.csv', 'w', 'utf-8')

#Get metadata of new datasets
print 'Total: ' + str(count)
pages = count/200 + 1 #total number of pages

for i in range(1, pages+1):
	print 'Getting data from page ' + str(i) + ' ...'
	
	urlhandle = urllib2.urlopen("http://nycopendata.socrata.com/api/views.json?limit=200&page=" + str(i))
	content = urlhandle.read()
	js = json.loads(content)

	for j in range(0, len(js)):

		temp = js[j]['id']

		if temp not in hmm:

			urlstr = "http://data.cityofnewyork.us/resource/%s.json" %temp

			try:		
				urlholder = urllib2.urlopen(urlstr, timeout=25)

				x = urlholder.read()
				jjss = json.loads(x)

				tempstr = ''
		
				if len(jjss) == 0:
					tempstr = 'No_Record'
		
				else:
					for key in jjss[0]:
						tempstr = tempstr + ' ' + key

			except urllib2.URLError, e:
				tempstr = 'Connection_failed'

			except socket.timeout:
				tempstr = 'Connection_failed'


			tagstr = ''

			if js[j].has_key('category'):
				tagstr = tagstr + ' ' + js[j]['category']

			if js[j].has_key('description'):
				xyz = js[j]['description']
				z = string.replace(xyz,'\n',' ')
				y = string.replace(z,'\r','') 
				tagstr = tagstr + ' ' + y
		
			if js[j].has_key('tags'):
				for t in js[j]['tags']:
					tagstr = tagstr + ' ' + t

			line = js[j]['id'] + '\t' +\
				js[j]['name'] + '\t' +\
				tempstr + '\t' + tagstr + '\n'

			#Write to file			
			f.write(line)
			new_count = new_count + 1
			print temp + ' ' + str(new_count) 


print 'Done'
f.close()

