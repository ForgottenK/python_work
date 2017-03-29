class User():
	def __init__(self, first_name, last_name, age, location):
		self.first_name = first_name
		self.last_name = last_name
		self.age = age
		self.location = location
		self.login_attempts = 0

	def describe_user(self):
		print("User's name : " + (self.first_name + " " + self.last_name).title() + 
			" age : " + str(self.age) + 
			" location : " + self.location)

	def greet_user(self):
		print('Hello, ' + (self.first_name + " " + self.last_name).title())

	def increment_login_attempts(self):
		self.login_attempts += 1

	def reset_login_attempts(self):
		self.login_attempts = 0

user = User('frank', 'king', 25, 'beijing')
user.describe_user()
user.greet_user()

user1 = User('storm', 'zhang', 30, 'shanghai')
user1.describe_user()
user1.greet_user()
print(user1.login_attempts)
user1.increment_login_attempts()
user1.increment_login_attempts()
print(user1.login_attempts)
user1.increment_login_attempts()
print(user1.login_attempts)
user1.reset_login_attempts()
print(user1.login_attempts)
