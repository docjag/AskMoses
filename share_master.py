#!/home/sohel/anaconda2/bin/python
# -*- coding: utf-8 -*-

# @Author: Sohel Mahmud
# @Date: 01.07.17
# @Python Version: 2.7.13 (Anaconda)
# @Description: Read the csv file of SHARE-EU and the create the report
# The sanity checks are as follows:
# 					1. Empty cells
# 					2. Duplicates
#					3. Numbering
#					4. Translation


import re
import csv
from bs4 import BeautifulSoup
from collections import OrderedDict


# Language-Country map dictionary
lang_dict = {
	'Germany': 'deDE',
	'Austria': 'deAT',
	'Malta': {
		'English': 'enMT',
		'Maltese': 'mtMT'
	},
	'France': 'frFR'
}


## Cleaning the HTML tags and other symbols from the data filefrom the string with BeautifulSoup
def clean_file(file_name):

	with open('SHARE_sample.csv','rb') as fh:
		lines = csv.reader(fh)
		for line in lines:
			print line
			clean_lines = []

			for field in line:
				print field
				cleantext = BeautifulSoup(field,'lxml').text
				cleantext = cleantext.strip()
				cleantext = cleantext.encode('utf-8')
				print cleantext
				
				clean_lines.append(cleantext)

			with open('clean_SHARE_sample.csv','ab') as cl_fh:
				csv_wr = csv.writer(cl_fh, quoting=csv.QUOTE_ALL)
				csv_wr.writerow(clean_lines)


# Blank check -- sanity check1
def blank_check(text):
	
	if text == '':
		print 'blank field'
		return 1

	else:
		return ""


# Duplicate check -- Sanity Check2
#Read the responses from the csv file of SHARE-EU and Split multiple answers

def duplicate_check():
	resp_dict = OrderedDict()

	with open('clean_SHARE_sample.csv','rb') as fh:
		lines = csv.reader(fh)
		lines.next()

		for line in lines:
			sanity_check2 = 0

			share_id = line[0].strip()
			item = line[1].strip().split('_')[0] + '_' + 'resp' + '_a'
			qtext = line[5].strip()

			ans = qtext.split('\n')

			for i in range(len(ans)):
				ans[i] = ans[i].strip()
				item_resp =  item + str(i + 1)

				if resp_dict.has_key(ans[i]):
					sanity_check2 = 1

					print 'dulicate found'

				else:
					resp_dict[ans[i]] = item_resp
				
				print item_resp, ans[i], sanity_check2


def check_numbering():



# check the fillers: 
# The fillers are as follows:
# With FL:
# 	1. /FLDefault[12]
# 	2. [{--FLDefault[94]--}]
# 	3. [{--FLLastInterviewMonthYear--}]
# 	4. [{--FLChildName--}]
# 	5. [{--FLCurr--}]
# 	6. [{--FLLastYear--}]
# 	7. [{--FLLastMonthYear--}]
# 	8. [FL_HH001_1] 
# 	9. [Thinking of the first of these relationships, what/What/Thinking of your'+FLNumber+' marriage, what] was your partner's first name?
# 	10. <FL>
# With others: 
#	1.
#	2.

def check_fillers(text):

	# For String having -FL- substring
	fl_words = re.findall('\S+FL\S+', text)
	print fl_words

	# for [{String}] format regular expression
	test1 = re.findall('.*[{[^ ]*}]',text)
	print test1

	# for [{String}] format regular expression
	test2 = re.findall('.*[[^ ]*]',text)
	print test2


# function for writing the header in the Report
def write_report_header():

	fitness = u'Fitness(\u03C3)'.encode('utf-8')
	distance = u'Distance(\u03B4)'.encode('utf-8')
	col_titles = ['ITEM','Lang','Generic English','Source Text','Sanity Check1','Sanity Check2','Sanity Check3','Sanity Check4','Moses Check1','Back Translation',fitness, distance,'Flag']


	with open('Report.csv','wb') as cl_fh:
				csv_wr = csv.writer(cl_fh, quoting=csv.QUOTE_ALL)
				csv_wr.writerow(col_titles)



def qtext():
	with open('clean_SHARE_sample.csv','rb') as fh:
		lines = csv.reader(fh)
		first_line = next(lines)
		
		country = first_line[11].split(' ')[2].strip('()')
		lang_id = lang_dict[country]

		for line in lines:
			break

		name = line[1].split('_')[0] + '_'
		item = name + 'Qtext'
		generic_english = line[7]
		#source_text = line[7+4]
		source_text = ""

		print item
		print lang_id
		print generic_english
		print source_text

		with open('Report.csv','ab') as cl_fh:
			csv_wr = csv.writer(cl_fh, quoting=csv.QUOTE_ALL)
			csv_wr.writerow([item,lang_id,generic_english, source_text, blank_check(source_text)])



########################################################################################
									#Main Body
########################################################################################

# Writing the header in the csv file
#writerow_report_header()

# Getting the QText
qtext()
