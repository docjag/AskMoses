import csv

# with open('SHARE_sample.csv','rb') as fh:
# 	reader = csv.DictReader(fh)

# 	for line in reader:
# 		headers = line.keys()
# 		break;

# 	for item in headers:
# 	    if item.startswith('QbyQ'):
# 	    	headers.remove(item)
	    
# 	    elif item == 'Name' or item == 'ID':
# 	    	headers.remove(item)

# 	header_size = len(headers)


suffix = ['QText','IWER','','']

with open('SHARE_sample.csv','rb') as fh:
	reader = csv.DictReader(fh)
	
	for row in reader:
		item = row['Name'].split('_')[0]
		
		for i in range(header_size):
			print item + '_'+ headers[i]