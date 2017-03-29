people = {
	'leiminghao': ['bed', 'hotel', 'motel'],
	'gengyuanbo': ['bed', 'hotel', 'motel'],
	'wangruixiang': ['library', 'company', 'gym'],
}
for k, v in people.items():
	print(k + ' likes stay in')
	for place in v:
		print('\t' + place + '\t')
	print()