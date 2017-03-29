cats_file = 'cats.txt'
dogs_file = 'dogs.txt'
try:
	with open(cats_file) as cat_f_obj:
		cats = cat_f_obj.readlines()
	with open(dogs_file) as dog_f_obj:
		dogs = dog_f_obj.readlines()
	message = 'The name of the cats : \n'
	for cat in cats:
		message += cat
	message += '\nThe name of the dogs : \n'
	for dog in dogs:
		message += dog
	print(message)
except FileNotFoundError:
	#print('can not find text file!')
	pass