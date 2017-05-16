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



# cleanr = re.compile('<.*?>')
# cleantext = re.sub(cleanr, '', field)


import csv
from bs4 import BeautifulSoup

blank_count = 0

with open('SHARE_sample.csv','rb') as fh:
	lines = csv.reader(fh)
	for line in lines:
		for field in line:
			#print field
			cleantext = BeautifulSoup(field,'lxml').text
			cleantext = cleantext.strip()
			#print cleantext
			
			if cleantext == '':
				print 'blank field'
				blank_count = blank_count + 1

	print blank_count