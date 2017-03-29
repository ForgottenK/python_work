from user import User

class Privileges():
	def __init__(self):
		self.privileges = ['can add post', 'can delete post', 'can ban user']

	def show_privileges(self):
		message = ''
		for privilege in self.privileges:
			message += privilege + ' '
		print(message)



class Admin(User):
	def __init__(self, first_name, last_name, age, location):
		super().__init__(first_name, last_name, age, location)
		self.privileges = Privileges()

admin = Admin('frank', 'king', 25, 'beijing')
admin.describe_user()
admin.privileges.show_privileges()