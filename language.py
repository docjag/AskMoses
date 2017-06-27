#!/home/sohel/anaconda2/bin/python

# @Author: Sohel Mahmud	
# @Date: 16.05.2017
# @Description: Clustering the countries according to the same languages
# @Last Status: CSV file has been created. Yet to be clustered the countries


import csv

header = ['Language', 'Country Name', 'Country Code','Data Release1','Data Release2','language Code']

with open('language_code.csv','ab') as fh_csv:
				csv_wr = csv.writer(fh_csv, quoting=csv.QUOTE_ALL)
				csv_wr.writerow(header)

with open('language.txt','rb') as fh:
	for line in fh:
		line = line.strip()
		words = line.split(' ')
		print words

		while '' in words:
			words.remove('')

		print words
		if words:
			with open('language_code.csv','ab') as fh_csv:
				csv_wr = csv.writer(fh_csv, quoting=csv.QUOTE_ALL)
				csv_wr.writerow(words)