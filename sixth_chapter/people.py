person = {'first_name': 'frank', 'last_name': 'king', 'age': 25, 'city': 'beijing'}
print(person['first_name'])
print(person['last_name'])
print(person['age'])
print(person['city'])

person_1 = {'first_name': 'eric', 'last_name': 'zheng', 'age': 32, 'city': 'beijing'}
person_2 = {'first_name': 'kobe', 'last_name': 'bryant', 'age': 39, 'city': 'los angeles'}

person_list = [person, person_1, person_2]
for p in person_list:
	print(p)