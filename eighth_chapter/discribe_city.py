def describe_city(name, country='china'):
	print(name.title() + ' is in ' + country.title())
describe_city('beijing')
describe_city('shanghai')
describe_city('los angeles', 'united states')