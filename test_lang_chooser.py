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
from bs4 import BeautifulSoup
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

lang_list = []

language = raw_input('Enter the name of the language: ',)
language = 'QText ' + language.title()
print language

with open('clean_SHARE_all.csv','rb') as fh:
	lines = csv.reader(fh)
	first_line = next(lines)
	for i in first_line:
		if language in i:
			lang_list.append(first_line.index(i))


print lang_list
