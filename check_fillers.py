#!/home/sohel/anaconda2/bin/python
# -*- coding: utf-8 -*-

# @Author: Sohel Mahmud
# @Date: 15.05.17
# @Description: Read the csv file of SHARE-EU and 
#               check the fillers
# The fillers are as follows:
# 1. /FLDefault[12]
# 2. [{--FLDefault[94]--}]
# 3. [{--FLLastInterviewMonthYear--}]
# 4. [{--FLChildName--}]
# 5. [{--FLCurr--}]
# 6. [{--FLLastYear--}]
# 7. [{--FLLastMonthYear--}]
# 8. [FL_HH001_1] 
# 9. [Thinking of the first of these relationships, what/What/Thinking of your'+FLNumber+' marriage, what] was your partner's first name?
#10. <FL>



import csv
import re

with open('clean_SHARE_sample.csv','rb') as fh:
	lines = csv.reader(fh)
	lines.next()

	for line in lines:
		# qtext = line[3]
		for cols in line:

			# For String having -FL- substring
			fl_words = re.findall('\S+FL\S+',cols)
			print fl_words

			# for [{String}] format regular expression
			test1 = re.findall('.*[{[^ ]*}]',cols)
			print test1

			# for [{String}] format regular expression
			test2 = re.findall('.*[[^ ]*]',cols)
			print test2