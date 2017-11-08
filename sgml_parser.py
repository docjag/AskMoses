#!/home/sohel/anaconda2/bin/python
# -*- coding: utf-8 -*-

# @Author: Sohel Mahmud
# @Date: 25.10.17
# @Python Version: 2.7.13 (Anaconda)
# @Description: Parse sgml file to parallel text

from bs4 import BeautifulSoup
import codecs

#################################################
############ Main body of the program: ##########
#################################################

file_name = raw_input("Enter the name of the file: ")
lang = raw_input("Enter language code: ")

with codecs.open(file_name,'r', encoding = 'utf-8') as fhand:
	for line in fhand:
		line = line.strip()
		soup = BeautifulSoup(line,'lxml')    # txt is simply the a string with your XML file
		pageText = soup.findAll(text=True)
		new_line = ' '.join(pageText).strip()
		if new_line is not "":
			print new_line
			with open('/home/sohel/sgm3txt.' + lang,'ab') as fh_write:
				fh_write.write(new_line.encode('utf-8') + '\n')
