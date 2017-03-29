favorite_number = {}
favorite_number['wangruixiang'] = [1, 2, 3, 4, 5]
favorite_number['leiminghao'] = [6, 7, 8]
favorite_number['wuyaru'] = [9, 10, 11]
favorite_number['gengyuanbo'] = [12, 13]
favorite_number['doujianmei'] = [14, 15, 16]
print(favorite_number['wangruixiang'])
print(favorite_number['leiminghao'])
print(favorite_number['wuyaru'])
print(favorite_number['gengyuanbo'])
print(favorite_number['doujianmei'])

for k, v in favorite_number.items():
	print(k + "'s favorite number is ")
	for value in v:
		print(value)