#!/usr/bin/python
# -*- coding: utf-8 -*-

# @Author: Sohel Mahmud
# @Date: 08.07.17
# @Python Version: 2.7.13 (Anaconda)
# @Description: Read the csv file of SHARE-EU and the create the report
# The sanity checks are as follows:
# 					1. Blank cell check
# 					2. Duplicate cell check
#					3. Number format check
#					4. Fillers check


import re
import csv
from collections import OrderedDict

## Country-Language map dictionary
# lang_dict = {
# 	'Generic': 'enEN',
# 	'Germany': 'deDE',
# 	'Austria': 'deAT',
# 	'Malta': {
# 		'English': 'enMT',
# 		'Maltese': 'mtMT'
# 	},
# 	'France': 'frFR',
# 	'Switzerland':{
# 		'French': 'frCH',
# 		'German':'deCH',
# 		'Italian':'itCH'
# 	},
# 	'Belgium': {
# 		'French': 'frBE',
# 		'Dutch': 'nlBE'
# 	},
# 	'Luxembourg': {
# 		'French':'frLU',
# 		'German':'deLU'
# 	}

# }

# Language-Country map dictionary
# ? languages an ?? countries
lang_dict = {
	'German':
	{
		'Germany':'deDE',
		'Austria':'deAT',
		'Switzerlang':'deCH',
		'Luxembourg':'deLU'
	},
	'French':
	{
		'France':'frFR',
		'Switzerland':'frCH',
		'Luxembourg':'frLU',
		'Belgium': 'frBE'	
	},
	'Maltese':
	{
		'Malta': 'mtMT'
	}
}



## Cleaning the HTML tags and other symbols from the data file from the string with BeautifulSoup
def clean_file(file_name):

	with open(file_name,'rb') as fh:
		
		lines = csv.reader(fh)

		first_line = next(lines)
		first_line[7] = 'QText English (Generic)'
		first_line[8] = 'Iwer_instruction English (Generic)'
		first_line[9] = 'Answer English (Generic)'
		first_line[10] = 'QbyQ English (Generic)'

		with open('clean_SHARE_all.csv','ab') as cl_fh:
			csv_wr = csv.writer(cl_fh, delimiter=',', quoting=csv.QUOTE_ALL)
			csv_wr.writerow(first_line)

		for line in lines:
			clean_lines = []

			for field in line:
				print field
				cleanr = re.compile('<.*?>')
				cleantext = re.sub(cleanr, '', field)
				cleantext =  re.sub(' +',' ', cleantext).strip()
				#cleantext = cleantext.decode('utf-8')
				print cleantext
				
				clean_lines.append(cleantext)

			with open('clean_SHARE_all.csv','ab') as cl_fh:
				csv_wr = csv.writer(cl_fh, delimiter=',', quoting=csv.QUOTE_ALL)
				csv_wr.writerow(clean_lines)

# Picking the language from the data file

def language_picker(file_name):

	lang_list = []

	fl_lang = raw_input('Enter the name of the language: ',).title()
	print fl_lang
	language = 'QText ' + fl_lang

	with open(file_name,'rb') as fh:
		lines = csv.reader(fh)
		first_line = next(lines)
		for i in first_line:
			if language in i:
				lang_list.append(first_line.index(i))

	print lang_list
	return lang_list, fl_lang



# Blank check -- sanity check1
def blank_check(text):
	
	text = text.strip(' ')
	if text == '':
		print 'blank field'
		return "1"

	elif text.startswith('_'):
		print 'blank field'
		return "1"

	else:
		return ""

# Checking the format ot the number  -- Sanity check3
# 		1. text1 = '100. ^MN002_Person[1].Name'
# 		2. text2 = '(1900..2017)'
def check_numbering(text):

	if text == "":
		return ""

	if text[0].isdigit():
		
		if re.findall('^[0-9]+\.\s.*',text):
			return ""

		elif re.findall('^\([0-9\.]+\)$',text):
			return ""

		else:
			return "1"


# check the fillers: -- Sanity Check4
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
# 	9. [Thinking of the first of these relationships, what/What/Thinking of your'+FLNumber+' marriage, what] 
#		was your partner's first name?
# 	10. <FL>
# With others: 
#	1. ^MN_Person[1]
#	2. []
def check_fillers(text):

	# For String having -FL- substring
	if re.findall('\S+FL\S+', text):
		return "1"

	# for [{String}] format regular expression
	elif re.findall('.*[{[^ ]*}]',text): 
		return "1"

	else:
		return ""


# function for writing the header in the Report
def write_report_header():

	fitness = u'Fitness(\u03C3)'.encode('utf-8')
	distance = u'Distance(\u03B4)'.encode('utf-8')
	# col_titles = ['ITEM','Lang','Generic English','Source Text','Sanity Check1','Sanity Check2','Sanity Check3','Sanity Check4','Moses Check1','Back Translation',fitness, distance,'Flag']
	col_titles = ['ITEM','Lang','Generic English','Source Text','Sanity Check1','Sanity Check2','Sanity Check3','Sanity Check4']


	with open('Report.csv','wb') as cl_fh:
				csv_wr = csv.writer(cl_fh, delimiter=',', quoting=csv.QUOTE_ALL)
				csv_wr.writerow(col_titles)


def report_write(item, lang, text_en, text_fl, check1, check2, check3, check4):
	with open('Report.csv','ab') as cl_fh:
			csv_wr = csv.writer(cl_fh, delimiter=',', quoting=csv.QUOTE_ALL)
			csv_wr.writerow([item, lang, text_en, text_fl, check1, check2, check3, check4])


def split_resp(item, resp_eng, resp_fl):
	resp_dict = OrderedDict()

	resp_eng = resp_eng.strip()
	resp_fl = resp_fl.strip()

	ans_eng = resp_eng.split('\n')
	ans_fl = resp_fl.split('\n')
			
	for i in range(len(ans_fl)):
		en_fl_list = []
		item_resp =  item + str(i + 1)
		print item_resp

		ans_eng[i] = ans_eng[i].strip()
		ans_fl[i] = ans_fl[i].strip()

		en_fl_list.extend([ans_eng[i],ans_fl[i]]) 

		resp_dict[item_resp] = en_fl_list

	return resp_dict


#################################################
############ Main body of the program: ##########
#################################################

file_name = 'SHARE_all.csv'

#clean_file(file_name)
write_report_header()

# Generic Engish start from index 7 (QText English (Generic))
eng = 7
#fl_list = [eng]
fl_list, flang = language_picker(file_name)
#fl_list.extend(lpicker_list)

with open('clean_SHARE_all.csv','rb') as fh:
	lines = csv.reader(fh)
	first_line = next(lines)

	ans_list = []

	for line in lines:

		name = line[1].split('_')[0] + '_'
		
		for fl in fl_list:
			country = first_line[fl].split(' ')[2].strip('()')
			print flang

			lang_id = lang_dict[flang][country]

			print 'language ID: ',lang_id

			# For QTEXT
			item = name + first_line[fl].split(' ')[0]
			print 'QTEXT: ',item
			print line[fl]

			if blank_check(line[fl]) == '1':
				report_write(item, lang_id, line[eng], line[fl], "1", "","", "")

			else:
				report_write(item, lang_id, line[eng], line[fl], "", "", check_numbering(line[fl]), check_fillers(line[fl]))

			
			# for IWER
			item = name + first_line[fl + 1].split(' ')[0].split('_')[0]
			print item, line[fl + 1]

			if blank_check(line[fl+1]) == '1':
				report_write(item, lang_id, line[eng + 1], line[fl + 1], "1", "","", "")

			else:
				report_write(item, lang_id, line[eng + 1], line[fl + 1], "", "", check_numbering(line[fl + 1]), check_fillers(line[fl+1]))


			# For Response
			item = name + first_line[fl + 2].split(' ')[0] + '_' + 'resp' + '_a'

			if blank_check(line[fl + 2]) == '1':
				report_write(item, lang_id, val[0], val[1], "1", "","", "")

			else:
				
				## Duplicate Answer check
				# if line[fl + 2] in ans_list:
				# 	sanity_check2 = '1'

				# else:
				# 	ans_list.append(line[fl + 2])
				# 	sanity_check2 = ''

				print len(line[fl + 2])
				print type(line[fl + 2])
				print line[fl + 2]

				test_dict = split_resp(item, line[eng + 2], line[fl + 2])

				for key, val in test_dict.items():
					print key, val[1]
					report_write(key, lang_id, val[0], val[1], "", "", check_numbering(val[1]), check_fillers(val[1]))	

				print '\n'


print ans_list
print len(ans_list)

