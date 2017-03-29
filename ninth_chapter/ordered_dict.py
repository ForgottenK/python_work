from collections import OrderedDict

words = OrderedDict()
words['list'] = 'a container that contains a series of objects'
words['variable'] = 'one object that can be assigned a value'
words['const'] = 'the objects that can not be modified after assigned'
words['print'] = 'a function can put some variable or sentences on the screen'
words['boolean'] = 'a type of variable only can be True or False'

for k, v in words.items():
	print(k + '\n\t' + v)