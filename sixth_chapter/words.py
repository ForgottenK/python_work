words = {
	'list': 'a container that contains a series of objects',
	'variable': 'one object that can be assigned a value',
	'const': 'the objects that can not be modified after assigned',
	'print': 'a function can put some variable or sentences on the screen',
	'boolean': 'a type of variable only can be True or False',
}
#print('list\n\t' + words['list'])
#print('variable\n\t' + words['variable'])
#print('const\n\t' + words['const'])
#print('print\n\t' + words['print'])
#print('boolean\n\t' + words['boolean'])
for k, v in words.items():
	print(k + '\n\t' + v)