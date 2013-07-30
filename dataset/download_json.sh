cat ../metadata/data/idlist_all.txt | while read LINE 
do
	if [ ! -f json/$LINE.json ]
	then
		wget -t 1 --output-document=json/$LINE.json --timeout=10 "https://data.cityofnewyork.us/api/views/$LINE/rows.json?accessType=DOWNLOAD"
	fi
done


