from restaurant import Restaurant

class IceCreamStand(Restaurant):
	def __init__(self, restaurant_name, cuisine_type):
		super().__init__(restaurant_name, cuisine_type)
		self.flavors = ['strawberry', 'watermelon', 'pineapple']

	def all_flavor(self):
		message = ''
		for flavor in self.flavors:
			message += (flavor + ' ')
		print(message)

ice_cream_stand = IceCreamStand('McDonalds sweety', 'snacks')
ice_cream_stand.describe_restaurant()
ice_cream_stand.all_flavor()