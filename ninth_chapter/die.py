from random import randint
class Die():
	def __init__(self, sides=6):
		self.sides = sides
	def roll_die(self):
		print(randint(1, self.sides))

die_six = Die()
for x in range(0,10):
	die_six.roll_die()
print()
die_ten = Die(10)
for x in range(0,10):
	die_ten.roll_die()
print()
die_20 = Die(20)
for x in range(0,10):
	die_20.roll_die()