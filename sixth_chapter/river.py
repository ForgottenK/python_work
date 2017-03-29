rivers = {'nile': 'egypt', 'amazon': 'south america', 'mississippi': 'united states'}
for k, v in rivers.items():
	print('The ' + k.title() + ' runs through ' + v.title())
for river in rivers.keys():
	print(river)
for nation in rivers.values():
	print(nation)