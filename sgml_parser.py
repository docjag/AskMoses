#!/home/sohel/anaconda2/bin/python
# -*- coding: utf-8 -*-

# @Author: Sohel Mahmud
# @Date: 25.10.17
# @Python Version: 2.7.13 (Anaconda)
# @Description: Parse sgml file to parallel text

from bs4 import BeautifulSoup

#################################################
############ Main body of the program: ##########
#################################################

file_name = raw_input("Enter the name of the file: ")
lang = raw_input("Enter language code: ")

with open(file_name,'rb') as fhand:
	for line in fhand:
		line = line.strip()
		soup = BeautifulSoup(line)    # txt is simply the a string with your XML file
		pageText = soup.findAll(text=True)
		new_line = ' '.join(pageText).strip()
		if new_line is "":
			print new_line
		else:
			with open('/home/sohel/sgm2txt.' + lang,'ab') as fh_write:
				fh_write.write(new_line.encode('utf-8') + '\n')
