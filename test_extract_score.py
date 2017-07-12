#!/home/sohel/anaconda2/bin/python
# -*- coding: utf-8 -*-

# @Author: Sohel Mahmud
# @Date: 12.07.17
# @Python Version: 2.7.13 (Anaconda)
# @Description: Extract the translation score from the terminal output file


#################################################
############ Main body of the program: ##########
#################################################


count = 0
str_score = '[total='
best = 'BEST TRANSLATION'
with open('terminal.out','rb') as fh:
	for line in fh:
		line = line.strip()
		if best in line:
			index = line.find(best)
			items = line[index:].split(' ')
			item = items[2].split('|')[0] 
			lang = items[4][0:4]
			

			score_indx = line.find(str_score)
			score = line[score_indx:].split(' ')[0][7:-1]
			print item, lang, score

			count += 1
#print count