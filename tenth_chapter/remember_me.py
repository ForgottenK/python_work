import json

def get_stored_username():
	"""get username if has stored it"""
	filename = 'username.json'
	try:
		with open(filename) as f_obj:
			username = json.load(f_obj)
	except FileNotFoundError:
		return None
	else:
		return username

def get_new_username():
	"""let user input username"""
	filename = 'username.json'
	username = input('What is your name? ')
	with open(filename, 'w') as f_obj:
		json.dump(username, f_obj)
	print('We will remember you when you come back, ' + username + '!')

def check_username(username):
	"""check the username is user's name"""
	right_username = input('Is your name ' + username + '?(y/n)')
	if right_username == 'n':
		get_new_username()
	else:
		print('Welcome back! ' + username)

def greet_user():
	"""greet user and print username"""
	username = get_stored_username()
	if username:
		check_username(username)
	else:
		get_new_username()

greet_user()