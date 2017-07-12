#!/home/sohel/anaconda2/bin/python
# -*- coding: utf-8 -*-

# @Author: Sohel Mahmud
# @Date: 12.07.17
# @Python Version: 2.7.13 (Anaconda)
# @Description: Merge the translation score the translated file


import re 

#################################################
############ Main body of the program: ##########
#################################################

with open('test.out','rb') as fh:
	for line in fh:
		print line
		if re.compile('\S+_QText',line):
			print line