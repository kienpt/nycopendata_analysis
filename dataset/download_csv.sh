cat ../metadata/data/idlist_all.txt | while read LINE 
do
	echo $LINE
	if [ ! -f csv/$LINE.csv ]
	then
		wget -t 1 --output-document=csv/$LINE.csv --timeout=10 "https://data.cityofnewyork.us/api/views/$LINE/rows.csv?accessType=DOWNLOAD"
	fi
done
