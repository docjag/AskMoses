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



import csv


fitness = u'Fitness(\u03C3)'.encode('utf-8')
distance = u'Distance(\u03B4)'.encode('utf-8')
col_titles = ['ITEM','Mod','Lang','Source Text','Sanity Check1','Sanity Check2','Sanity Check3','Moses Check1','Back Translation',fitness, distance,'Flag']


with open('Report.csv','wb') as cl_fh:
			csv_wr = csv.writer(cl_fh, quoting=csv.QUOTE_ALL)
			csv_wr.writerow(col_titles)


header = []
flag = False

with open('SHARE_sample.csv','rb') as fh:
	lines = csv.reader(fh)
	for line in lines:
		if flag == False:
			header = line
			flag = True

		item = line[1].split('_')[0]
		mod = item[:2]
		print type(item)

