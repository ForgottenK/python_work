def make_sandwich(*ingredients):
	print('\nHere is the ingredients of the sandwich:')
	for ingredient in ingredients:
		print('- ' + ingredient)

make_sandwich('tomato', 'spicy', 'bacon')
make_sandwich('cucumber', 'onion')
make_sandwich('potato', 'ham')