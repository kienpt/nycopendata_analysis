import json
import urllib
from datetime import datetime

#Get the total number of datasets
urlhandle = urllib.urlopen('http://nycopendata.socrata.com/api/views.json?count=True')
content = urlhandle.read()
js = json.loads(content)
print js['count']

#Write the number to file
f = open('counter.csv', 'a')
f.write(str(datetime.now()) + '\t' + str(js['count']) + '\n')
f.close()
