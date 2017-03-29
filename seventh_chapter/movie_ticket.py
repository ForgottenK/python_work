active = True
while active:
	age = input('Please input the audience\'s age: ')
	age = int(age)
	if age < 0:
		break
	if age < 3:
		print('Free.')
	elif age <= 12:
		print('$10.')
	else:
		print('$15.')