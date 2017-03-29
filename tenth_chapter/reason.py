filename = 'programming_reason.txt'
with open(filename, 'a') as file_object:
	while True:
		reason = input('Please input a reason that why you love progamming: ')
		if reason:
			file_object.write(reason + '\n')
		else:
			break