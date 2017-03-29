dream_destination = {}
while True:
	name = input('Please input your name: ')
	if name == '':
		break
	destination = input('If you could visit one place in the world,'
		+ 'where would you go? ')
	dream_destination[name] = destination
print('---Result---')
for k, v in dream_destination.items():
	print(k.title() + '\'s dream destination is ' + v.title())