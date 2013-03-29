
import socket
import string
import urllib2

f = open('without_duplicate.csv','r')

for line in f:
	temp = line
	words = temp.split()

	temp = words[0]

	tempstr = 'qqq'

	urlstr = "http://data.cityofnewyork.us/resource/%s.json" %temp

	try:		
		urlholder = urllib2.urlopen(urlstr, timeout=25)
		x = urlholder.read()

		foo = open(temp,'w')

		foo.write(x)
		print temp
		foo.close()

	except urllib2.URLError, e:
		tempstr = 'Connection_failed'

	except socket.timeout:
		tempstr = 'Connection_failed'

		
