#!/usr/bin/python
# -*- coding: utf-8 -*-

# @Author: Sohel Mahmud
# @Date: 11.07.17
# @Python Version: 2.7.13 (Anaconda)
# @Description: Read the csv file for the back translation
#               population the data in the report


import csv


with open('output-fr','rb') as fh:
	lines = csv.reader(fh)
	for line in lines:
		print line
		if line:
			print line[0], line[1]
			with open('translate_French.csv','ab') as cl_fh:
					csv_wr = csv.writer(cl_fh, quoting=csv.QUOTE_ALL)
					csv_wr.writerow([fields[0], fields[1], fields[3]])
print first_line