#!/home/sohel/anaconda2/bin/python
# -*- coding: utf-8 -*-

# @Author: Sohel Mahmud
# @Date: 08.07.17
# @Python Version: 2.7.13 (Anaconda)
# @Description: Read the csv file of SHARE-EU and the create the report

import csv

#################################################
############ Main body of the program: ##########
#################################################

with open('Report.csv','rb') as fh:
	lines = csv.reader(fh)
	first_line = next(lines)

	counter = 0

	for fields in lines:
		if '1' in [fields[4],fields[5], fields[6], fields[7]]:
			continue

		else:
			print fields[0], fields[1], fields[3]
			counter += 1
			with open('translate.csv','ab') as cl_fh:
					csv_wr = csv.writer(cl_fh, quoting=csv.QUOTE_ALL)
					csv_wr.writerow([fields[0], fields[1], fields[3]])

	print counter