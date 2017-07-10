#!/home/sohel/anaconda2/bin/python
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

# Language-Country map dictionary
lang_dict = {
	'Generic': 'enEN',
	'Germany': 'deDE',
	'Austria': 'deAT',
	'Malta': {
		'English': 'enMT',
		'Maltese': 'mtMT'
	},
	'France': 'frFR',
	'Switzerland':{
		'French': 'frCH',
		'German':'deCH',
		'Italian':'itCH'
	},
	'Belgium': {
		'French': 'frBE',
		'Dutch': 'nlBE'
	},
	'Luxembourg': {
		'French':'frLU',
		'German':'deLU'
	}

}



# Blank check -- sanity check1
def blank_check(text):
	
	text = text.strip(' ')
	if text == '':
		print 'blank field'
		return "1"

	else:
		return ""

def check_numbering(text):
	# text = '100. ^MN002_Person[1].Name'
	# text2 = 'We need $455 for the enrollment'
	# text3 = '(1900..2017)'

	if text == "":
		return ""

	if re.findall('^[0-9]+\.\s.*',text):
		return ""

	elif re.findall('^\([0-9\.]+\)$',text):
		return ""

	else:
		return "1"

def check_fillers(text):

	# For String having -FL- substring
	if re.findall('\S+FL\S+', text):
		return "1"

	# for [{String}] format regular expression
	elif re.findall('.*[{[^ ]*}]',text): 
		return "1"

	# for [{String}] format regular expression
	elif re.findall('.*[[^ ]*]',text):
		return "1"

	else:
		return ""



def report_write(item, lang, text_en, text_fl, check2):
	with open('test.csv','ab') as cl_fh:
			csv_wr = csv.writer(cl_fh, quoting=csv.QUOTE_ALL)
			csv_wr.writerow([item, lang, text_en, text_fl, check2])


def split_resp(item, resp_eng, resp_fl):
	resp_dict = OrderedDict()

	resp_eng = resp_eng.strip()
	resp_fl = resp_fl.strip()

	ans_eng = resp_eng.split('\n')
	ans_fl = resp_fl.split('\n')
			
	for i in range(len(ans_eng)):
		en_fl_list = []
		item_resp =  item + str(i + 1)

		ans_eng[i] = ans_eng[i].strip()
		ans_fl[i] = ans_fl[i].strip()

		en_fl_list.extend([ans_eng[i],ans_fl[i]]) 

		resp_dict[item_resp] = en_fl_list

	return resp_dict


#################################################
############ Main body of the program: ##########
#################################################

with open('clean_SHARE_sample.csv','rb') as fh:
	lines = csv.reader(fh)
	first_line = next(lines)

	ans_list = []

	for line in lines:

		name = line[1].split('_')[0] + '_'

		eng = 7
		start = 11
		end = len(first_line)
		
		for fl in range(start,end,4):
			country = first_line[fl].split(' ')[2].strip('()')
			lang_id = lang_dict[country]

			print 'lang: ',lang_id

			# For Response
			item = name + first_line[fl + 2].split(' ')[0] + '_' + 'resp' + '_a'

			if line[fl + 2] in ans_list:
				sanity_check2 = '1'

			else:
				ans_list.append(line[fl + 2])
				sanity_check2 = ''

			test_dict = split_resp(item, line[eng + 2], line[fl + 2])

			for key, val in test_dict.items():
				report_write(key, lang_id, val[0], val[1], sanity_check2)

	print ans_list
	print len(ans_list)