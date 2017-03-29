class Restaurant():
	def __init__(self, restaurant_name, cuisine_type):
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type
		self.number_served = 0

	def describe_restaurant(self):
		print('Restaurant_name : ' + self.restaurant_name.title() + 
			', cuisine_type : ' + self.cuisine_type)

	def open_restaurant(self):
		print('The ' + self.restaurant_name.title() + ' is opening.')

	def set_number_served(self, number_served):
		self.number_served = number_served

	def increment_number_served(self, number_served):
		self.number_served += number_served

restaurant = Restaurant('shaXian snacks', 'snacks')
restaurant.describe_restaurant()
restaurant.open_restaurant()

restaurant1 = Restaurant("McDonald's", "snacks")
restaurant1.describe_restaurant()

restaurant2 = Restaurant('KFC', 'snacks')
restaurant2.describe_restaurant()

restaurant3 = Restaurant('Dicos', 'snacks')
print('This restaurant have served ' + str(restaurant3.number_served) + ' people.')
restaurant3.set_number_served(3)
print('This restaurant have served ' + str(restaurant3.number_served) + ' people.')
restaurant3.increment_number_served(100)
print('This restaurant have served ' + str(restaurant3.number_served) + ' people.')
