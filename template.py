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


# function for cleaning the texts
def clean_text():


# function for counting the blank cells
def blank_count():
	
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


# function for writing the header in the Report
def write_report_header():

	fitness = u'Fitness(\u03C3)'.encode('utf-8')
	distance = u'Distance(\u03B4)'.encode('utf-8')
	col_titles = ['ITEM','Mod','Lang','Source Text','Sanity Check1','Sanity Check2','Sanity Check3','Moses Check1','Back Translation',fitness, distance,'Flag']


	with open('Report.csv','wb') as cl_fh:
				csv_wr = csv.writer(cl_fh, quoting=csv.QUOTE_ALL)
				csv_wr.writerow(col_titles)