#!/home/sohel/anaconda2/bin/python
# -*- coding: utf-8 -*-

# @Author: Sohel Mahmud
# @Date: 15.05.17
# @Description: Read the responses from the csv file of SHARE-EU and 
#     			Split multiple answers



import csv
from collections import OrderedDict

resp_dict = OrderedDict()

with open('clean_SHARE_sample.csv','rb') as fh:
	lines = csv.reader(fh)
	lines.next()

	for line in lines:

		share_id = line[0].strip()
		item = line[1].strip().split('_')[0] + '_' + 'resp' + '_a'
		qtext = line[5].strip()

		ans = qtext.split('\n')

		for i in range(len(ans)):
			ans[i] = ans[i].strip()
			item_resp =  item + str(i + 1)

			print item_resp, ans[i]

			if resp_dict.has_key(item_resp):
				ref = resp_dict[item_resp]
				print item_resp, resp_dict[item_resp]
				print ref


        	else:
        		resp_dict[item_resp] = ans[i]
        		print item_resp, resp_dict[item_resp]