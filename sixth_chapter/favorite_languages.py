favorite_languages = {'wangruixiang': 'python', 'gengyuanbo': 'java', 'wuyaru': 'objective-c'}
persons = ['wangruixiang', 'gengyuanbo', 'wuyaru', 'leiminghao', 'doujianmei']
for person in persons:
	if person in favorite_languages:
		print(person.title() + ', thank you for taking the poll.')
	else:
		print(person.title() + ', please take our poll!')