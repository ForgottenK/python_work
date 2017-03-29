age = 90
if age < 2:
	stage = 'baby'
elif age < 4:
	stage = 'learning steps'
elif age < 13:
	stage = 'children'
elif age < 20:
	stage = 'teenager'
elif age < 65:
	stage = 'adult'
else:
	stage = 'elder'
print('this people is ' + stage)