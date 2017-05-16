#!/home/sohel/anaconda2/bin/python
# -*- coding: utf-8 -*-

# @Author: Sohel Mahmud
# @Date: 15.05.17
# @Description: 



# cleanr = re.compile('<.*?>')
# cleantext = re.sub(cleanr, '', field)


import csv
import re
from bs4 import BeautifulSoup


data = '''
<br />

sfjslfjfjsdlfj
fsdfjsdlfjsdl
sffjsdlfj

<br />
'''
#print data

# cleanr = re.compile('<.*?>\n')
# cleantext = re.sub(cleanr, '', data)
# cleantext = cleantext.strip()
# print cleantext

cleantext = BeautifulSoup(data,'lxml').text
cleantext = cleantext.strip()
print cleantext