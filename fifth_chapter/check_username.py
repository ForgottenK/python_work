current_users = ['susan', 'james', 'anthony', 'steve', 'dannis']
new_users = ['JAmes', 'michael', 'karl', 'george', 'steve']
for new_user in new_users:
	if new_user.lower() in current_users:
		print('user name exists, please try another.')
	else:
		print('user name not exist yet.')
