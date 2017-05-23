#!/home/sohel/anaconda2/bin/python
# -*- coding: utf-8 -*-

# @Author: Sohel Mahmud
# @Date: 15.05.17
# @Description: Read the responnses from the csv file of SHARE-EU and 
#     			Split multiple answers



import csv

with open('clean_SHARE_sample.csv','rb') as fh:
	lines = csv.reader(fh)
	lines.next()

	for line in lines:
		qtext = line[5].strip()

		ans = qtext.split('\n')
		for i in range(len(ans)):
			print ans[i]
