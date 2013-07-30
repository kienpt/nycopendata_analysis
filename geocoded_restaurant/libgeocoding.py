#!/usr/bin/python
import urllib
import sys

def geocode(building_number, street_name, zipcode):
	address = building_number + ' ' + street_name + ', ' + zipcode
	try:
		url = 'http://rpc.geocoder.us/service/csv?address=' + address
		content = urllib.urlopen(url).read()
		coordinate = content.split(',')
		if len(coordinate) > 2:
			return (coordinate[0], coordinate[1]) #[lat, lon]
		else:
			return address
	except urllib.URLError, e:
		print ("There was an error %r" % e)
		return address

def main(argv):
	print geocode('536', '77th', '11209')

if __name__=="__main__":
	main(sys.argv[1:])
	
