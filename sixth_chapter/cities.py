cities = {
	'beijing': {
		'country': 'china',
		'population': 21520000,
		'fact': 'holded 2008 olympic games',
	},
	'seoul': {
		'country': 'south korea',
		'population': 10140000,
		'fact': 'have many beautiful girls',
	},
	'tokyo': {
		'country': 'japan',
		'population': 13507300,
		'fact': 'is the capital of japan',
	}
}

for k, v in cities.items():
	print(k + '\t' + str(v))
