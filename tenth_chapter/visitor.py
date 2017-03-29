filename = 'guest.txt'
with open(filename, 'w') as file_object:
	username = input('please input you name :')
	file_object.write(username)