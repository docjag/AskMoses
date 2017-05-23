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



suffix = ['QText','IWER','','']

with open('SHARE_sample.csv','rb') as fh:
	reader = csv.DictReader(fh)
	
	for row in reader:
		item = row['Name'].split('_')[0]
		
		for i in range(header_size):
			print item + '_'+ headers[i]