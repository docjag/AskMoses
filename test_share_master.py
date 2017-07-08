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
	
	text = text.strip(' ')
	if text == '':
		print 'blank field'
		return "1"

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



def check_numbering(text):
	# text = '100. ^MN002_Person[1].Name'
	# text2 = 'We need $455 for the enrollment'
	# text3 = '(1900..2017)'

	test1 = re.findall('^[0-9]+\.\s.*',text)
	print test1

	test2 = re.findall('^\([0-9\.]+\)$',text)
	print test2

	text4 = 'a'
	test3 = re.findall('ab*',text)
	print test3

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


def report_write(item, lang, text_en, text_fl, check1):
	with open('Report.csv','ab') as cl_fh:
			csv_wr = csv.writer(cl_fh, quoting=csv.QUOTE_ALL)
			csv_wr.writerow([item, lang, text_en, text_fl, check1])


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



with open('clean_SHARE_sample.csv','rb') as fh:
	lines = csv.reader(fh)
	first_line = next(lines)

	for line in lines:
		if line[0] == 3720:
			break

	name = line[1].split('_')[0] + '_'

	eng = 7
	start = 11
	end = len(first_line)
	
	for fl in range(start,end,4):
		country = first_line[fl].split(' ')[2].strip('()')
		lang_id = lang_dict[country]

		print 'lang: ',lang_id

		# For QTEXT
		item = name + first_line[fl].split(' ')[0]
		print 'QTEXT: ',item
		print line[fl]

		report_write(item, lang_id, line[eng], line[fl], blank_check(line[eng]))
		
		# for IWER
		item = name + first_line[fl + 1].split(' ')[0].split('_')[0]
		print item, line[fl + 1]
		print line[eng + 1] == ''
		print blank_check(line[eng + 1])

		report_write(item, lang_id, line[eng + 1], line[fl + 1], "1")

		
		# For Response
		item = name + first_line[fl + 2].split(' ')[0] + '_' + 'resp' + '_a'

		#test_dict = split_resp(item, resp)
		test_dict = split_resp(item, line[eng + 2], line[fl + 2])

		for key, val in test_dict.items():
			print key, val[1]
			report_write(key, lang_id, val[0], val[1], blank_check(val[0]))

		print '\n'
