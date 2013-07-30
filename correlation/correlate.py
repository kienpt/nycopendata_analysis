import sys

#path = "../311service/complaint_type/erm2-nwe9/"
f1 = sys.argv[1]
lat1 = 2 #index of lattitude attribute
lon1 = 3 #index of longitude attribute
f2 = sys.argv[2]
lat2 = 3
lon2 = 2

#The rectangle that circumscribes the NYC area
lat_min = 40.496222
lon_min = -74.275818
lat_max = 40.905383
lon_max = -73.591919


#Number of cells = x*y
x = 300
y = 300
x = int(sys.argv[3])
y = int(sys.argv[4])
lon_cell = (lon_max - lon_min)/x
lat_cell = (lat_max - lat_min)/y

def isInRec(lat, lon):
	if (lat < lat_min) | (lat > lat_max):
		return False
	if (lon < lon_min) | (lon > lon_max):
		return False
	return True

def partition(f, lat, lon):
	cells = [[0 for i in range(y)] for j in range(x)]
	count = 0
	with open(f) as fi:
		for line in fi:
			count += 1
			a = line.strip('\n').split('\t')
			_lon = float(a[lon])
			_lat = float(a[lat])
			if isInRec(_lat, _lon):
				_x = int(round((_lon - lon_min)/lon_cell - 0.5))
				_y = int(round((_lat - lat_min)/lat_cell - 0.5))
				cells[_x][_y] += 1
#			else:
#				print "Wrong point"
	return (cells, count)

(cells1, size1)  = partition(f1, lat1, lon1)
(cells2, size2)  = partition(f2, lat2, lon2)
ratios = [[0 for i in range(y)] for j in range(x)]

for i in range(0, x):
	for j in range(0, y):
		if cells1[i][j] == 0 & cells2[i][j] == 0:
			continue
		if cells1[i][j] == 0:
			ratios[i][j] = cells2[i][j] + 1
		elif cells2[i][j] == 0:
			ratios[i][j] = 1/float(cells1[i][j] + 1)
		else:
			ratios[i][j] = (cells2[i][j] + cells1[i][j])*cells2[i][j]/float(cells1[i][j]) 
score = 0
count = 0
for i in range(0, x):
	for j in range(0, y):
		if ratios[i][j] != 0:
			count += 1
			score = score + ratios[i][j]
score = score*(size1/float(size2))/float(size1 + size2) #Normalization	
print count
print size1
print size2
print (size1+size2)/float(count)
print score
