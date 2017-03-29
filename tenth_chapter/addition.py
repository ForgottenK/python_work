while True:
	number_one = input('please input a number :')
	number_two = input('please input another number : ')
	if number_one and number_two:
		try:
			answer = int(number_one) + int(number_two)
		except ValueError:
			print('please input integer number!')
		else:
			print(answer)
	else:
		break