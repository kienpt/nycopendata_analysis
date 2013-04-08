#Download all non-duplicated datasets
#Each dataset is written to a file
import socket
import string
import urllib2

succ = 0 #Count number of successfull downloads
fail = 0 #Count number of fail downloads
f_log = open('log.txt', 'w')
f_fail = open('faildownload.txt', 'w') #Store ids of fail downloaded datasets
f_succ = open('succdownload.txt', 'w') #Store ids of successful downloaded datasets

with open('without_duplicate.csv') as lines:
	for line in lines:
		words = line.split()
		_id = words[0]
		tempstr = 'qqq'
		urlstr = "http://data.cityofnewyork.us/resource/%s.json" %_id

		try:		
			urlholder = urllib2.urlopen(urlstr, timeout=25)
			x = urlholder.read()

			f_out = open('dataset/' + _id + '.json','w')
			f_out.write(x)
			f_out.close()

			succ += 1
			if succ % 10 == 0:
				print succ
			f_succ.write(_id + '\n')
		except urllib2.URLError, e:
			print 'Connection_failed'
			fail += 1
			f_fail.write(_id + '\n')

		except socket.timeout:
			print 'Connection_failed'
			fail += 1
			f_fail.write(_id + '\n')
f_log.write('Number of successful downloads: ' + str(succ) + '\n')
f_log.write('Number of fail downloads: ' + str(fail) + '\n')
f_log.close()
f_fail.close()
f_succ.close()

		
