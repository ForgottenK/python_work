import json

filename = 'favorite_number.json'

try:
	with open(filename) as f_obj:
		favorite_number = json.load(f_obj)
except FileNotFoundError:
	print('can not find favorite_number.json!')
else:
	print(favorite_number)