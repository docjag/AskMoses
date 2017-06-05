import re

text = '100. ^MN002_Person[1].Name'
text2 = 'We need $455 for the enrollment'
text3 = '(1900..2017)'

test1 = re.findall('^[0-9]+\.\s.*',text)
print test1

test2 = re.findall('^\([0-9\.]+\)$',text3)
print test2

text4 = 'a'
test3 = re.findall('ab*',text4)
print test3
