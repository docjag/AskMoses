
with open('lang_head.txt','rb') as fin, open('countries.txt','wb') as fout:
	for line in fin.readlines()[0::4]:
		line = line.strip()
		words = line.split(' ')
		language = words[1]
		country = words[2]
		print language
		country = country.strip('()')
		print country

		country_code = 'DE'
		lang_code = 'de'

		# fout.write(language + ',' + country + ','+ country_code + ',' + lang_code)
		fout.write(language + ',' + country)
		fout.write('\n')

# with open('lang_head.txt','rb') as fh:
# 	countries = ''.join(fh.readlines()[0::4]).split(' ')
# 	size = len(countries)
# 	print countries
# 	for i in range(2,size,2):
# 		print countries[i]

with open('language_code.csv','rb') as fh:
	for line in fh:
		line = line.strip()
		lang_code = line.split(',')[4]
		print lang_code