filename = 'guest_book.txt'
with open(filename, 'w') as file_object:
	while True:
		username = input('Please input you name : ')
		if username:
			file_object.write(username + '\n')
			print('Welcome ! ' + username.title())
		else:
			break