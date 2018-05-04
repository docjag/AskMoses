#!/usr/bin/python
# -*- coding: utf-8 -*-

# @Author: Sohel Mahmud
# @Date: 03.04.18
# @Python Version: Python 2.7.14
# @Description: Remove the quotation marks from the csv file
#

with open('/home/docjag/test.fr','rb') as fhand:
	for line in fhand:
		line = line.replace('"','').strip()

		with open('/home/docjag/test_new.fr','ab') as fwrite:
			fwrite.write(line  + '\n')

