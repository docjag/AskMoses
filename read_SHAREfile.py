#!/home/sohel/anaconda2/bin/python

# @Author: Sohel Mahmud
# @Date: 15.05.17
# @Description: Read the csv file of SHARE-EU and 
#               execute the Sanity checks.
# The sanity checks are as follows:
# 					1. Empty cells
# 					2. Duplicates
#					3. Numbering
#					4. Translation

# Note:
# -----
# # Cleaning the HTML tags from the string with BeautifulSoup
# from bs4 import BeautifulSoup
# cleantext = BeautifulSoup(line,'lxml').text
# print cleantext




import re
import csv

with open('/home/sohel/share-eu.csv','rb') as fh:

	for line in fh:
		line = line.strip()
		# # Cleaning the HTML tags from the string with Regular Expression	
		cleanr = re.compile('<.*?>')
		cleantext = re.sub(cleanr, '', line)
		print cleantext
	print cleantext

