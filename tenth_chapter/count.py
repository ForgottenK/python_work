filename = 'cats.txt'
with open(filename) as f_obj:
	content = f_obj.read()
print(content.lower().count('y'))