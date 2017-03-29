from user import User
from admin import Admin

my_user = Admin('frank', 'king', 25, 'beijing')
my_user.describe_user()
my_user.privileges.show_privileges()

guest = User('guest', 'noname', 0, 'local')
guest.describe_user()