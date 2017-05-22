#!/home/sohel/anaconda2/bin/python
# -*- coding: utf-8 -*-

# @Author: Sohel Mahmud
# @Date: 15.05.17
# @Description: Read the csv file of SHARE-EU and 
#               execute the Sanity checks.
# The sanity checks are as follows:
# 					1. Empty cells
# 					2. Duplicates
#					3. Numbering
#					4. Translation



import csv
from bs4 import BeautifulSoup

blank_count = 0

with open('SHARE_sample.csv','rb') as fh:
	lines = csv.reader(fh)
	for line in lines:
		print line
		clean_lines = []

		for field in line:
			print field
			cleantext = BeautifulSoup(field,'lxml').text
			cleantext = cleantext.strip()
			cleantext = cleantext.encode('utf-8')
			print cleantext
			
			if cleantext == '':
				print 'blank field'
				cleantext = 1
				blank_count = blank_count + 1

			if clean_lines = 'sfs':
				pass
				

			clean_lines.append(cleantext)

		with open('clean_SHARE_sample.csv','ab') as cl_fh:
			csv_wr = csv.writer(cl_fh, quoting=csv.QUOTE_ALL)
			csv_wr.writerow(clean_lines)


	print blank_count
