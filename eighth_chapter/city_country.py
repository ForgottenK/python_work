def city_country(city, country):
	return '"' + city.title() + ', ' + country.title() + '"'
print(city_country('beijing', 'china'))
print(city_country('shanghai', 'china'))
print(city_country('los angeles', 'united states'))