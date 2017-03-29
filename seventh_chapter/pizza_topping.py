message = ''
while message != 'quit':
	message = input('Please input a kind of pizza topping: ')
	if message != 'quit':
		print('We will add ' + message + ' in the pizza.')