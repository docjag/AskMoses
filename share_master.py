#!/home/sohel/anaconda2/bin/python
# -*- coding: utf-8 -*-

# @Author: Sohel Mahmud
# @Date: 15.05.17
# @Python Version: 2.7.13 (Anaconda)
# @Description: Read the csv file of SHARE-EU and the report


import re
import csv
from bs4 import BeautifulSoup


# function for writing the header in the Report
def write_report_header():

	fitness = u'Fitness(\u03C3)'.encode('utf-8')
	distance = u'Distance(\u03B4)'.encode('utf-8')
	col_titles = ['ITEM','Mod','Lang','Source Text','Sanity Check1','Sanity Check2','Sanity Check3','Moses Check1','Back Translation',fitness, distance,'Flag']


	with open('Report.csv','wb') as cl_fh:
				csv_wr = csv.writer(cl_fh, quoting=csv.QUOTE_ALL)
				csv_wr.writerow(col_titles)


def 