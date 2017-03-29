def make_car(manufacturer, model, **car_info):
	car = {}
	car['manufacturer'] = manufacturer
	car['model'] = model
	for k, v in car_info.items():
		car[k] = v
	return car

car = make_car('subaru', 'outback', color='blue', tow_package=True)
print(car)